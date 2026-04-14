from __future__ import annotations

import argparse
from pathlib import Path

from mvp.openai_utils import build_client, chunked, invoke_json_model, load_records_payload, save_json, utc_timestamp


DEFAULT_REWRITE_PROMPT_LABEL = "quality_rewrite_official_openai_style_v1"


REWRITE_SCHEMA = {
    "type": "object",
    "properties": {
        "rewrites": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "improved_candidate_ko": {"type": "string"},
                },
                "required": ["id", "improved_candidate_ko"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["rewrites"],
    "additionalProperties": False,
}


def _source_text(record: dict, field: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing string field '{field}' for {record.get('id', 'unknown-record')}")
    return value.strip()


def _build_eval_hints(path: str | None) -> dict[str, dict]:
    if not path:
        return {}

    _, records = load_records_payload(Path(path))
    hints_by_id: dict[str, dict] = {}
    for record in records:
        hints_by_id[record["id"]] = {
            "overall_score": record.get("overall_score"),
            "issues": record.get("issues", []),
            "review_reasons": record.get("review_reasons", []),
            "suggested_revision": record.get("suggested_revision"),
        }
    return hints_by_id


def _backfill_missing_rewrites(
    client,
    *,
    model: str,
    instructions: str,
    batch: list[dict],
    rewrites_by_id: dict[str, str],
    eval_hints_by_id: dict[str, dict],
    source_field: str,
    max_attempts: int = 3,
) -> None:
    requested_ids = {record["id"] for record in batch}
    missing_ids = requested_ids - rewrites_by_id.keys()
    attempts = 0

    while missing_ids and attempts < max_attempts:
        payload_items = []
        for record in batch:
            if record["id"] not in missing_ids:
                continue
            item = {
                "id": record["id"],
                "source_en": record["source_en"],
                "reference_ko": record["reference_ko"],
                "candidate_ko": _source_text(record, source_field),
            }
            eval_hint = eval_hints_by_id.get(record["id"])
            if eval_hint:
                item["eval_hint"] = eval_hint
            payload_items.append(item)

        result = invoke_json_model(
            client,
            model=model,
            instructions=instructions,
            payload={"items": payload_items},
            schema_name="candidate_rewrite_retry_batch",
            schema=REWRITE_SCHEMA,
            max_output_tokens=7000,
        )
        for item in result["rewrites"]:
            item_id = item["id"]
            if item_id in missing_ids:
                rewrites_by_id[item_id] = item["improved_candidate_ko"].strip()
        missing_ids = requested_ids - rewrites_by_id.keys()
        attempts += 1

    if missing_ids:
        raise ValueError(f"Missing improved candidates after retries: {sorted(missing_ids)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rewrite first-pass Korean candidates into stronger publication-ready Korean.",
    )
    parser.add_argument("--input", required=True, help="Candidate artifact created by generate_candidate.py.")
    parser.add_argument(
        "--output",
        default=None,
        help="Output path. Defaults to data/processed/<input-stem>.improved.json",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.4",
        help="Rewrite model used for quality refinement.",
    )
    parser.add_argument(
        "--source-field",
        default="candidate_ko",
        help="Candidate field to rewrite. Defaults to candidate_ko.",
    )
    parser.add_argument(
        "--eval-input",
        default=None,
        help="Optional eval JSON used to pass score/issues/suggested revision as rewrite hints.",
    )
    parser.add_argument("--batch-size", type=int, default=6, help="Number of blocks rewritten per request.")
    parser.add_argument("--run-label", default=None, help="Optional run label preserved on the output artifact.")
    parser.add_argument("--pipeline-label", default=None, help="Optional pipeline label preserved on the output artifact.")
    parser.add_argument(
        "--prompt-label",
        default=DEFAULT_REWRITE_PROMPT_LABEL,
        help="Optional rewrite prompt label preserved on the output artifact.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    meta, records = load_records_payload(input_path)
    client = build_client()
    eval_hints_by_id = _build_eval_hints(args.eval_input)

    instructions = (
        "You are rewriting Korean translations for an official OpenAI-style publication. "
        "For each item, use source_en as the meaning source, candidate_ko as the first-pass draft, "
        "and reference_ko only as a supporting reference for style and terminology. "
        "Produce one improved_candidate_ko that preserves the factual meaning, improves Korean fluency, "
        "tightens style, and increases terminology consistency. "
        "Do not blindly copy reference_ko or mirror it sentence-by-sentence. "
        "Keep product names, benchmark names, inline code, numbers, percentages, and list structure stable. "
        "If eval hints are provided, use them to fix concrete issues, but keep the rewrite faithful to source_en. "
        "Return only the requested JSON schema."
    )

    rewrites_by_id: dict[str, str] = {}
    for batch in chunked(records, args.batch_size):
        payload_items = []
        for record in batch:
            item = {
                "id": record["id"],
                "source_en": record["source_en"],
                "reference_ko": record["reference_ko"],
                "candidate_ko": _source_text(record, args.source_field),
            }
            eval_hint = eval_hints_by_id.get(record["id"])
            if eval_hint:
                item["eval_hint"] = eval_hint
            payload_items.append(item)

        result = invoke_json_model(
            client,
            model=args.model,
            instructions=instructions,
            payload={"items": payload_items},
            schema_name="candidate_rewrite_batch",
            schema=REWRITE_SCHEMA,
            max_output_tokens=7000,
        )
        for item in result["rewrites"]:
            rewrites_by_id[item["id"]] = item["improved_candidate_ko"].strip()
        _backfill_missing_rewrites(
            client,
            model=args.model,
            instructions=instructions,
            batch=batch,
            rewrites_by_id=rewrites_by_id,
            eval_hints_by_id=eval_hints_by_id,
            source_field=args.source_field,
        )

    enriched_records = []
    for record in records:
        improved_candidate = rewrites_by_id.get(record["id"])
        if not improved_candidate:
            raise ValueError(f"Missing improved candidate for {record['id']}")
        enriched_record = dict(record)
        enriched_record["improved_candidate_ko"] = improved_candidate
        enriched_records.append(enriched_record)

    output_path = Path(args.output or f"data/processed/{input_path.stem}.improved.json")
    output_meta = dict(meta)
    if args.run_label:
        output_meta["run_label"] = args.run_label
    if args.pipeline_label:
        output_meta["pipeline_label"] = args.pipeline_label

    save_json(
        output_path,
        {
            **output_meta,
            "rewritten_at": utc_timestamp(),
            "rewrite_model": args.model,
            "rewrite_source_field": args.source_field,
            "rewrite_output_field": "improved_candidate_ko",
            "rewrite_prompt_label": args.prompt_label,
            "rewrite_hint_input": args.eval_input,
            "records": enriched_records,
        },
    )
    print(f"Wrote {len(enriched_records)} improved candidates to {output_path}")


if __name__ == "__main__":
    main()
