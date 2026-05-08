from __future__ import annotations

import argparse
from pathlib import Path

from mvp.openai_utils import load_records_payload


RECOMMENDED_GENERATION_MODEL = "gpt-5.5"
RECOMMENDED_REWRITE_MODEL = "gpt-5.5"
CLEAR_IMPROVEMENT_THRESHOLD = 1.0


def _evaluated_candidate_text(record: dict) -> str:
    value = record.get("evaluated_candidate_ko") or record.get("candidate_ko") or ""
    return value.strip() if isinstance(value, str) else ""


def _candidate_field_label(field: str | None) -> str:
    if field == "candidate_ko":
        return "first-pass candidate"
    if field == "improved_candidate_ko":
        return "improved candidate"
    if field:
        return f"`{field}`"
    return "unknown candidate field"


def _format_summary(summary: dict) -> str:
    return "\n".join(
        [
            f"- average_overall_score: {summary.get('average_overall_score', 0.0):.1f}",
            f"- average_semantic_similarity_score: {summary.get('average_semantic_similarity_score', 0.0):.1f}",
            f"- average_backtranslation_similarity_score: {summary.get('average_backtranslation_similarity_score', 0.0):.1f}",
            f"- average_terminology_consistency_score: {summary.get('average_terminology_consistency_score', 0.0):.1f}",
            f"- average_llm_judge_score: {summary.get('average_llm_judge_score', 0.0):.1f}",
            f"- human_review_count: {summary.get('human_review_count', 0)}",
        ]
    )


def _format_top_items(records: list[dict], *, field: str, limit: int) -> str:
    lines = []
    for record in sorted(records, key=lambda item: item[field])[:limit]:
        field_fragment = f"{field}={record[field]:.1f}"
        if field == "overall_score":
            field_fragment = f"overall={record['overall_score']:.1f}"
        lines.append(
            f"- `{record['id']}` | {field_fragment}\n"
            f"  evaluated_candidate: {_evaluated_candidate_text(record)}\n"
            f"  issues: {', '.join(record['issues']) if record['issues'] else 'none'}"
        )
    return "\n".join(lines) if lines else "- none"


def _format_review_list(records: list[dict]) -> str:
    flagged = [record for record in records if record.get("needs_human_review")]
    if not flagged:
        return "- none"

    lines = []
    for record in flagged:
        reasons = ", ".join(record.get("review_reasons", [])) or "issues present"
        lines.append(
            f"- `{record['id']}` | overall={record['overall_score']:.1f} | reasons: {reasons}"
        )
    return "\n".join(lines)


def _format_provenance(meta: dict, config: dict) -> str:
    generation_model = meta.get("generation_model", "n/a")
    rewrite_model = meta.get("rewrite_model", "n/a")
    backtranslation_model = config.get("backtranslation_model", "n/a")
    judge_model = config.get("judge_model", "n/a")
    embedding_model = config.get("embedding_model", "n/a")
    generated_at = meta.get("generated_at", "n/a")
    rewritten_at = meta.get("rewritten_at", "n/a")
    evaluated_at = meta.get("evaluated_at", "n/a")
    run_label = meta.get("run_label")
    pipeline_label = meta.get("pipeline_label")
    prompt_label = meta.get("prompt_label")
    rewrite_prompt_label = meta.get("rewrite_prompt_label")
    candidate_field = config.get("candidate_field")
    evaluated_stage = config.get("evaluated_stage")
    rewrite_source_field = meta.get("rewrite_source_field")
    rewrite_output_field = meta.get("rewrite_output_field")

    lines = [
        f"- generated_at: `{generated_at}`",
        f"- rewritten_at: `{rewritten_at}`",
        f"- evaluated_at: `{evaluated_at}`",
        f"- generation_model: `{generation_model}`",
        f"- rewrite_model: `{rewrite_model}`",
        f"- backtranslation_model: `{backtranslation_model}`",
        f"- judge_model: `{judge_model}`",
        f"- embedding_model: `{embedding_model}`",
    ]
    if candidate_field:
        lines.append(f"- candidate_field: `{candidate_field}`")
    if evaluated_stage:
        lines.append(f"- evaluated_stage: `{evaluated_stage}`")
    if rewrite_source_field:
        lines.append(f"- rewrite_source_field: `{rewrite_source_field}`")
    if rewrite_output_field:
        lines.append(f"- rewrite_output_field: `{rewrite_output_field}`")
    if run_label:
        lines.append(f"- run_label: `{run_label}`")
    if pipeline_label:
        lines.append(f"- pipeline_label: `{pipeline_label}`")
    if prompt_label:
        lines.append(f"- prompt_label: `{prompt_label}`")
    if rewrite_prompt_label:
        lines.append(f"- rewrite_prompt_label: `{rewrite_prompt_label}`")

    recorded_models = [generation_model, backtranslation_model, judge_model]
    rewrite_models = [rewrite_model]
    if any(model not in {"n/a", RECOMMENDED_GENERATION_MODEL} for model in recorded_models) or any(
        model not in {"n/a", RECOMMENDED_REWRITE_MODEL} for model in rewrite_models
    ):
        lines.append("")
        lines.append(
            "> Note: This report may reflect a non-default configuration. The current recommendation is `gpt-5.5` for first-pass generation, rewrite, backtranslation, and judging."
        )

    return "\n".join(lines)


def _build_comparison_rows(current_records: list[dict], compare_records: list[dict]) -> list[dict]:
    compare_by_id = {record["id"]: record for record in compare_records}
    rows = []
    for current in current_records:
        baseline = compare_by_id.get(current["id"])
        if not baseline:
            continue
        rows.append(
            {
                "id": current["id"],
                "delta": round(current["overall_score"] - baseline["overall_score"], 1),
                "before_score": baseline["overall_score"],
                "after_score": current["overall_score"],
                "before_candidate": _evaluated_candidate_text(baseline),
                "after_candidate": _evaluated_candidate_text(current),
                "current_issues": current.get("issues", []),
            }
        )
    return sorted(rows, key=lambda item: item["delta"], reverse=True)


def _format_improved_blocks(rows: list[dict], *, limit: int = 10) -> str:
    improved = [row for row in rows if row["delta"] >= CLEAR_IMPROVEMENT_THRESHOLD]
    if not improved:
        return "- none"

    lines = []
    for row in improved[:limit]:
        lines.append(
            f"- `{row['id']}` | overall_delta={row['delta']:+.1f} | before={row['before_score']:.1f} | after={row['after_score']:.1f}"
        )
    return "\n".join(lines)


def _format_before_after_examples(rows: list[dict], *, limit: int = 3) -> str:
    changed = [row for row in rows if row["delta"] > 0 and row["before_candidate"] != row["after_candidate"]]
    if not changed:
        return "- none"

    lines = []
    for row in changed[:limit]:
        issues = ", ".join(row["current_issues"]) if row["current_issues"] else "none"
        lines.append(
            f"- `{row['id']}` | overall_delta={row['delta']:+.1f}\n"
            f"  before: {row['before_candidate']}\n"
            f"  after: {row['after_candidate']}\n"
            f"  current_issues: {issues}"
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a human-readable markdown report from evaluation JSON.",
    )
    parser.add_argument("--input", required=True, help="Evaluation JSON created by run_eval.py.")
    parser.add_argument(
        "--compare-input",
        default=None,
        help="Optional baseline evaluation JSON used for before/after comparison.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output markdown path. Defaults to reports/<input-stem>.md",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    meta, records = load_records_payload(input_path)
    summary = meta.get("summary", {})
    config = meta.get("config", {})
    pair_slug = meta.get("pair_slug") or records[0].get("metadata", {}).get("pair_slug", "unknown-pair")

    compare_meta: dict = {}
    compare_records: list[dict] = []
    compare_summary: dict = {}
    compare_config: dict = {}
    comparison_rows: list[dict] = []
    if args.compare_input:
        compare_meta, compare_records = load_records_payload(Path(args.compare_input))
        compare_summary = compare_meta.get("summary", {})
        compare_config = compare_meta.get("config", {})
        comparison_rows = _build_comparison_rows(records, compare_records)

    terminology_mismatches = [record for record in records if record["terminology_consistency_score"] < 100]

    compare_section = ""
    if comparison_rows:
        compare_section = f"""
## First-Pass Candidate Summary

- candidate_field: `{compare_config.get("candidate_field", "candidate_ko")}` ({_candidate_field_label(compare_config.get("candidate_field"))})
{_format_summary(compare_summary)}

## Improved Candidate Summary

- candidate_field: `{config.get("candidate_field", "candidate_ko")}` ({_candidate_field_label(config.get("candidate_field"))})
{_format_summary(summary)}

## Improved Blocks

{_format_improved_blocks(comparison_rows)}

## Before / After Examples

{_format_before_after_examples(comparison_rows)}
"""
    else:
        compare_section = f"""
## Candidate Summary

- candidate_field: `{config.get("candidate_field", "candidate_ko")}` ({_candidate_field_label(config.get("candidate_field"))})
{_format_summary(summary)}

## Before / After Examples

- not available in this report. Pass `--compare-input <first-pass-eval.json>` to compare the rewritten candidate against a baseline evaluation.

## Improved Blocks

- not available in this report. Pass `--compare-input <first-pass-eval.json>` to compute score deltas.
"""

    report = f"""# Translation Evaluation Report

## Pair

- pair_slug: `{pair_slug}`
- unit_count: {summary.get("count", len(records))}
- score_scale: `{config.get("score_scale", "0-100")}`
- overall_formula: `{config.get("overall_formula", "n/a")}`

## Artifact Provenance

{_format_provenance(meta, config)}
{compare_section}

## Top 5 Problem Items

{_format_top_items(records, field="overall_score", limit=5)}

## Terminology Mismatch Examples

{_format_top_items(terminology_mismatches, field="terminology_consistency_score", limit=5)}

## Backtranslation Mismatch Examples

{_format_top_items(records, field="backtranslation_similarity_score", limit=5)}

## Still Needs Human Review

{_format_review_list(records)}
"""

    output_path = Path(args.output or f"reports/{input_path.stem}.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Wrote markdown report to {output_path}")


if __name__ == "__main__":
    main()
