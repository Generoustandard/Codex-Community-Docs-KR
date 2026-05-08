# OpenAI Review Packet

## Scope

This branch demonstrates a Phase 1 MVP for evaluating Korean translation quality on an official OpenAI English-Korean page pair.

Demo pair:

- English: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- Korean: https://openai.com/ko-KR/index/why-we-no-longer-evaluate-swe-bench-verified/

The current checked-in model-generated artifacts were refreshed with `gpt-5.5` on 2026-04-26. Human-reviewed golden examples were not regenerated or automatically changed.

## Current Pipeline

`source_en -> candidate_ko -> improved_candidate_ko -> evaluation -> human review -> reviewed_golden`

Current model configuration:

- `generation_model`: `gpt-5.5`
- `rewrite_model`: `gpt-5.5`
- `backtranslation_model`: `gpt-5.5`
- `judge_model`: `gpt-5.5`
- `embedding_model`: `text-embedding-3-small`

The two translation stages remain separate by prompt, stage metadata, and output field:

- `candidate_ko`: first-pass translation candidate
- `improved_candidate_ko`: rewrite/refinement candidate

## Main Artifacts

- `data/processed/why-we-no-longer-evaluate-swe-bench-verified.aligned.json`
- `data/processed/why-we-no-longer-evaluate-swe-bench-verified.aligned.candidates.json`
- `reports/why-we-no-longer-evaluate-swe-bench-verified.aligned.candidates.eval.json`
- `data/processed/why-we-no-longer-evaluate-swe-bench-verified.aligned.candidates.improved.json`
- `reports/why-we-no-longer-evaluate-swe-bench-verified.aligned.candidates.improved.eval.json`
- `reports/why-we-no-longer-evaluate-swe-bench-verified.report.md`
- `reports/golden.paragraphs.eval.json`

## Evaluation Summary

First-pass candidate evaluation:

- records: 46
- average overall score: 93.8
- average semantic similarity score: 90.5
- average backtranslation similarity score: 95.0
- average terminology consistency score: 99.5
- average LLM judge score: 93.4
- human-review flags: 2

Improved candidate evaluation:

- records: 46
- average overall score: 96.5
- average semantic similarity score: 95.8
- average backtranslation similarity score: 94.4
- average terminology consistency score: 100.0
- average LLM judge score: 97.3
- human-review flags: 0

Reviewed-golden paragraph check:

- approved reviewed-golden records: 8
- candidate field evaluated: `improved_candidate_ko`
- average candidate-vs-reviewed-golden score: 90.4
- average source-vs-backtranslation score: 88.7

## Human Review Boundary

- `reference_ko` is the official Korean page reference for Phase 1 pair evaluation.
- `reference_ko` is not automatically treated as golden.
- `candidate_ko` and `improved_candidate_ko` are model outputs and are not golden.
- `reviewed_golden` means a small maintainer-approved subset used for lightweight regression checks and future comparison.
- The current approved reviewed-golden subset lives in `docs/golden/paragraphs.json`.
- `docs/golden/words.json` and `docs/golden/sentences.json` are intentionally empty placeholders until official page-pair examples are curated.

## Checks Performed

- Verified script syntax for `generate_candidate.py`, `improve_candidate.py`, `run_eval.py`, `build_report.py`, `run_golden_eval.py`, and `evals/golden_loader.py`.
- Verified checked-in generated artifacts use `gpt-5.5` for generation, rewrite, backtranslation, and judging.
- Verified the improved candidate artifact contains both `candidate_ko` and `improved_candidate_ko`.
- Verified the improved evaluation evaluates `candidate_field = improved_candidate_ko`.
- Verified the golden paragraph eval uses `golden_target_field = reviewed_golden_ko`.
- Verified no older model references remain in the external-facing docs, scripts, or refreshed artifacts.
- Verified the markdown report is UTF-8 readable and contains no replacement characters.

## Non-Goals

- This MVP does not claim that community translations are better than the official Korean page.
- This MVP does not promote model output to golden automatically.
- Developer-document evaluation is left as a future Phase 2 extension.
