# Translation Evaluation Report

## Pair

- pair_slug: `why-we-no-longer-evaluate-swe-bench-verified`
- unit_count: 46
- score_scale: `0-100`
- overall_formula: `0.30 * semantic_similarity_score + 0.25 * backtranslation_similarity_score + 0.15 * terminology_consistency_score + 0.30 * llm_judge_score`

## Artifact Provenance

- generated_at: `2026-04-26T10:38:15.228608+00:00`
- rewritten_at: `2026-04-26T10:42:09.140756+00:00`
- evaluated_at: `2026-05-08T02:29:54.434785+00:00`
- generation_model: `gpt-5.5`
- rewrite_model: `gpt-5.5`
- backtranslation_model: `gpt-5.5`
- judge_model: `gpt-5.5`
- embedding_model: `text-embedding-3-small`
- candidate_field: `improved_candidate_ko`
- evaluated_stage: `rewrite`
- rewrite_source_field: `candidate_ko`
- rewrite_output_field: `improved_candidate_ko`
- run_label: `phase1-gpt-5.5-refresh`
- pipeline_label: `official-page-pair-two-stage`
- prompt_label: `quality_rewrite_official_openai_style_v1`
- rewrite_prompt_label: `quality_rewrite_official_openai_style_v1`
- post_generation_edits: `1`
- post_generation_edit: `why-we-no-longer-evaluate-swe-bench-verified.block-005` `improved_candidate_ko` - Maintainer wording review: replace awkward heading and clarify exam analogy while preserving source meaning.

## First-Pass Candidate Summary

- candidate_field: `candidate_ko` (first-pass candidate)
- average_overall_score: 93.8
- average_semantic_similarity_score: 90.5
- average_backtranslation_similarity_score: 95.0
- average_terminology_consistency_score: 99.5
- average_llm_judge_score: 93.4
- human_review_count: 2

## Improved Candidate Summary

- candidate_field: `improved_candidate_ko` (improved candidate)
- average_overall_score: 96.5
- average_semantic_similarity_score: 95.7
- average_backtranslation_similarity_score: 94.3
- average_terminology_consistency_score: 100.0
- average_llm_judge_score: 97.3
- human_review_count: 0

## Improved Blocks

- `why-we-no-longer-evaluate-swe-bench-verified.block-019` | overall_delta=+11.3 | before=79.2 | after=90.5
- `why-we-no-longer-evaluate-swe-bench-verified.block-003` | overall_delta=+8.2 | before=85.6 | after=93.8
- `why-we-no-longer-evaluate-swe-bench-verified.block-023` | overall_delta=+7.4 | before=89.0 | after=96.4
- `why-we-no-longer-evaluate-swe-bench-verified.block-022` | overall_delta=+6.6 | before=89.6 | after=96.2
- `why-we-no-longer-evaluate-swe-bench-verified.block-015` | overall_delta=+6.3 | before=93.1 | after=99.4
- `why-we-no-longer-evaluate-swe-bench-verified.block-044` | overall_delta=+5.9 | before=88.1 | after=94.0
- `why-we-no-longer-evaluate-swe-bench-verified.block-045` | overall_delta=+5.9 | before=89.1 | after=95.0
- `why-we-no-longer-evaluate-swe-bench-verified.block-005` | overall_delta=+5.4 | before=87.7 | after=93.1
- `why-we-no-longer-evaluate-swe-bench-verified.block-031` | overall_delta=+5.3 | before=91.1 | after=96.4
- `why-we-no-longer-evaluate-swe-bench-verified.block-016` | overall_delta=+4.9 | before=89.4 | after=94.3

## Before / After Examples

- `why-we-no-longer-evaluate-swe-bench-verified.block-019` | overall_delta=+11.3
  before: 지나치게 좁거나 지나치게 넓은 테스트
  after: 너무 제한적이거나 너무 광범위한 테스트
  current_issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-003` | overall_delta=+8.2
  before: 새로운 분석에서, 우리는 Verified 세트에서 오늘날의 성능 수준에서 frontier 출시를 위한 자율 소프트웨어 엔지니어링 역량의 진전을 측정하는 데 이 벤치마크가 더 이상 적합하지 않음을 보여주는 두 가지 주요 문제를 발견했습니다.
  after: 새로운 분석에서 Verified 세트의 두 가지 주요 문제를 발견했습니다. 이는 현재의 성능 수준에서 프런티어 모델 출시에 수반되는 자율 소프트웨어 엔지니어링 역량의 진전을 측정하는 데 이 벤치마크가 더 이상 적합하지 않음을 보여줍니다.
  current_issues: 'indicate'를 '보여줍니다'로 번역해 원문보다 다소 단정적으로 들릴 수 있음.
- `why-we-no-longer-evaluate-swe-bench-verified.block-023` | overall_delta=+7.4
  before: 점검한 과제 중 18.8%는 문제 설명에 명시되지 않은 추가 기능을 검사하는 테스트를 포함하고 있습니다. 우리는 이를 넓은 테스트 케이스라고 부릅니다.
  after: 감사 대상 과제의 18.8%에는 문제 설명에 명시되지 않은 추가 기능을 검사하는 테스트가 포함되어 있으며, 이를 광범위한 테스트 케이스라고 부릅니다.
  current_issues: reference의 '작업' 대신 '과제'를 사용했지만 의미상 허용 가능한 대체입니다.


## Top 5 Problem Items

- `why-we-no-longer-evaluate-swe-bench-verified.block-019` | overall=90.5
  evaluated_candidate: 너무 제한적이거나 너무 광범위한 테스트
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-002` | overall=92.5
  evaluated_candidate: 초기의 큰 도약 이후 SWE-bench Verified에서의 최고 성능(SOTA) 향상세는 둔화되어, 지난 6개월 동안 74.9%에서 80.9%로 개선되는 데 그쳤습니다. 이는 남아 있는 실패가 모델의 한계를 반영하는지, 아니면 데이터세트 자체의 특성을 반영하는지에 대한 질문을 제기합니다.
  issues: 'remaining failures'를 '남아 있는 실패'로 옮긴 표현은 약간 직역적이나 허용 가능함.
- `why-we-no-longer-evaluate-swe-bench-verified.block-012` | overall=92.8
  evaluated_candidate: 무관한 기존 기능이 그대로 유지되는지 확인하기 위해, 수정 전후에 모두 통과하는 회귀 테스트.
  issues: 'ensure'의 보장 뉘앙스가 '확인'으로 다소 약해졌지만 의미 전달에는 문제가 없습니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-024` | overall=92.9
  evaluated_candidate: 나머지 5.1%의 과제에는 이 분류 체계에 명확하게 속하지 않는 기타 문제가 있었습니다.
  issues: 'not well grouped'의 뉘앙스가 '명확하게 속하지 않는'으로 자연스럽게 처리되었으나 약간 의역되었습니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-005` | overall=93.1
  evaluated_candidate: 정답 학습: 대규모 프런티어 모델은 학습 과정에서 정보를 습득할 수 있으므로, 평가 대상이 되는 문제와 정답으로 모델을 절대 학습시키지 않는 것이 중요합니다. 이는 시험 문제와 답안을 미리 공유하는 것과 비슷합니다. 학생들이 답을 암기하지는 않더라도, 답을 미리 본 학생들은 그렇지 않은 학생들보다 분명히 더 좋은 성과를 낼 것입니다. SWE-bench 문제는 많은 모델 제공업체가 학습 목적으로 사용하는 오픈소스 저장소에서 가져온 것입니다. 이번 분석에서 테스트한 모든 프런티어 모델은 정답 기준으로 사용되는, 사람이 작성한 원본 버그 수정인 골드 패치나 특정 과제의 문제 설명 세부 문구를 그대로 재현할 수 있었습니다. 이는 이들 모두가 학습 중 최소한 일부 문제와 정답을 본 적이 있음을 시사합니다.
  issues: 시험 비유에서 'upcoming test with students before the test'의 구체성이 약간 축약됨., '정답'은 문맥상 가능하지만 '해답'이 solutions와 더 일관됨.

## Terminology Mismatch Examples

- none

## Backtranslation Mismatch Examples

- `why-we-no-longer-evaluate-swe-bench-verified.block-019` | backtranslation_similarity_score=61.8
  evaluated_candidate: 너무 제한적이거나 너무 광범위한 테스트
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-002` | backtranslation_similarity_score=80.4
  evaluated_candidate: 초기의 큰 도약 이후 SWE-bench Verified에서의 최고 성능(SOTA) 향상세는 둔화되어, 지난 6개월 동안 74.9%에서 80.9%로 개선되는 데 그쳤습니다. 이는 남아 있는 실패가 모델의 한계를 반영하는지, 아니면 데이터세트 자체의 특성을 반영하는지에 대한 질문을 제기합니다.
  issues: 'remaining failures'를 '남아 있는 실패'로 옮긴 표현은 약간 직역적이나 허용 가능함.
- `why-we-no-longer-evaluate-swe-bench-verified.block-032` | backtranslation_similarity_score=85.5
  evaluated_candidate: 아래는 여러 모델 제공업체에서 나타난 심각한 오염 사례입니다.
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-044` | backtranslation_similarity_score=85.6
  evaluated_candidate: 둘째, 자동화된 채점을 올바르게 구현하는 것은 까다롭습니다. 완벽한 테스트 케이스는 중요하지 않은 특정 구현 세부 사항에는 구애받지 않으면서도, 편법적인 해법에 흔들리지 않을 만큼 견고하게 기능이 올바르게 작동하는지 온전히 검증해야 합니다. 이러한 문제는 본질적으로 복잡하고 해결하기 어렵습니다. 이러한 문제를 찾아내는 데는 여러 차례의 대규모 수동 레이블링 작업이 필요했습니다.
  issues: “편법적인 해법에 흔들리지 않을 만큼”은 의미는 전달되지만 공식 기술 문서에서는 다소 구어적으로 느껴질 수 있음.
- `why-we-no-longer-evaluate-swe-bench-verified.block-016` | backtranslation_similarity_score=86.6
  evaluated_candidate: 많은 작업 명세가 충분히 구체적이지 않아 여러 가지 타당한 해석이 가능했지만, 테스트는 그중 특정 해석 하나만 다루고 있었습니다.
  issues: none

## Still Needs Human Review

- none
