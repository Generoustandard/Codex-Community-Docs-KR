# Translation Evaluation Report

## Pair

- pair_slug: `why-we-no-longer-evaluate-swe-bench-verified`
- unit_count: 46
- score_scale: `0-100`
- overall_formula: `0.30 * semantic_similarity_score + 0.25 * backtranslation_similarity_score + 0.15 * terminology_consistency_score + 0.30 * llm_judge_score`

## Artifact Provenance

- generated_at: `2026-04-05T03:38:20.863013+00:00`
- rewritten_at: `2026-04-13T02:15:10.161465+00:00`
- evaluated_at: `2026-04-13T02:16:49.147727+00:00`
- generation_model: `gpt-5.4-mini`
- rewrite_model: `gpt-5.4`
- backtranslation_model: `gpt-5.4-mini`
- judge_model: `gpt-5.4-mini`
- embedding_model: `text-embedding-3-small`
- candidate_field: `improved_candidate_ko`
- evaluated_stage: `rewrite`
- rewrite_source_field: `candidate_ko`
- rewrite_output_field: `improved_candidate_ko`
- rewrite_prompt_label: `quality_rewrite_official_openai_style_v1`

## First-Pass Candidate Summary

- candidate_field: `candidate_ko` (unknown candidate field)
- average_overall_score: 93.0
- average_semantic_similarity_score: 88.9
- average_backtranslation_similarity_score: 95.6
- average_terminology_consistency_score: 97.3
- average_llm_judge_score: 93.0
- human_review_count: 5

## Improved Candidate Summary

- candidate_field: `improved_candidate_ko` (improved candidate)
- average_overall_score: 95.8
- average_semantic_similarity_score: 94.2
- average_backtranslation_similarity_score: 94.2
- average_terminology_consistency_score: 100.0
- average_llm_judge_score: 96.7
- human_review_count: 0

## Improved Blocks

- `why-we-no-longer-evaluate-swe-bench-verified.block-041` | overall_delta=+17.8 | before=82.2 | after=100.0
- `why-we-no-longer-evaluate-swe-bench-verified.block-005` | overall_delta=+13.1 | before=81.2 | after=94.3
- `why-we-no-longer-evaluate-swe-bench-verified.block-003` | overall_delta=+9.1 | before=82.4 | after=91.5
- `why-we-no-longer-evaluate-swe-bench-verified.block-019` | overall_delta=+8.7 | before=83.6 | after=92.3
- `why-we-no-longer-evaluate-swe-bench-verified.block-038` | overall_delta=+8.1 | before=91.9 | after=100.0
- `why-we-no-longer-evaluate-swe-bench-verified.block-040` | overall_delta=+8.0 | before=85.7 | after=93.7
- `why-we-no-longer-evaluate-swe-bench-verified.block-035` | overall_delta=+5.8 | before=94.2 | after=100.0
- `why-we-no-longer-evaluate-swe-bench-verified.block-045` | overall_delta=+4.9 | before=92.0 | after=96.9
- `why-we-no-longer-evaluate-swe-bench-verified.block-001` | overall_delta=+4.8 | before=92.8 | after=97.6
- `why-we-no-longer-evaluate-swe-bench-verified.block-016` | overall_delta=+4.5 | before=88.7 | after=93.2

## Before / After Examples

- `why-we-no-longer-evaluate-swe-bench-verified.block-041` | overall_delta=+17.8
  before: Task ID: django__django-11099
  after: 작업 ID: django__django-11099
  current_issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-005` | overall_delta=+13.1
  before: 해결책에 대한 학습: 대형 최첨단 모델은 학습 과정에서 정보를 습득할 수 있으므로, 평가 대상인 문제와 해결책을 학습하지 않도록 하는 것이 매우 중요합니다. 이는 학생들에게 시험 전에 예정된 시험의 문제와 답을 미리 공유하는 것과 비슷합니다. 정답을 외우지 못할 수도 있지만, 답을 미리 본 학생이 그렇지 않은 학생보다 분명히 더 좋은 성과를 낼 것입니다. SWE-bench 문제는 많은 모델 제공업체가 학습 목적으로 사용하는 오픈소스 저장소에서 출처를 가져옵니다. 우리의 분석에서 테스트한 모든 최첨단 모델은 정답 참조로 사용되는 원래의 인간 작성 버그 수정, 즉 gold patch, 또는 특정 작업에 대한 문제 설명의 세부 사항을 그대로 재현할 수 있었으며, 이는 이들 모두가 학습 과정에서 적어도 일부 문제와 해결책을 보았음을 보여줍니다.
  after: 해답 학습: 대규모 프런티어 모델은 학습 과정에서 정보를 습득할 수 있으므로, 평가 대상이 되는 문제와 해답으로 모델을 절대 학습시키지 않는 것이 중요합니다. 이는 앞으로 치를 시험의 문제와 해답을 시험 전에 학생들에게 공유하는 것과 같습니다. 정답을 통째로 외우지는 않더라도, 해답을 미리 본 학생은 그렇지 않은 학생보다 분명히 더 좋은 성과를 낼 것입니다. SWE-bench 문제는 많은 모델 제공업체가 학습 목적으로 사용하는 오픈소스 리포지터리에서 추출됩니다. 이번 분석에서 테스트한 모든 프런티어 모델은 정답 기준으로 사용되는 사람이 작성한 원본 버그 수정인 `gold patch` 또는 특정 작업의 문제 설명에 담긴 세부 사항을 글자 그대로 재현할 수 있었으며, 이는 이들 모두가 학습 과정에서 최소한 일부 문제와 해답을 접했음을 보여줍니다.
  current_issues: “학생들에게”와 “성과”는 가능하지만, 원문 대비 약간 더 일반적인 표현입니다., 영문 괄호표현 `gold patch` 처리 방식은 자연스럽지만, 용어 일관성을 위해 한글 설명과 병기 형태를 더 정리할 수 있습니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-003` | overall_delta=+9.1
  before: 새로운 분석에서 우리는 Verified 세트에 두 가지 주요 문제가 있음을 확인했으며, 이는 이 벤치마크가 더 이상 오늘날의 성능 수준에서 최첨단 출시를 위한 자율 소프트웨어 엔지니어링 역량의 진전을 측정하는 데 적합하지 않음을 시사합니다:
  after: 새로운 분석에서 우리는 Verified 세트에 두 가지 주요 문제가 있음을 확인했으며, 이는 이 벤치마크가 오늘날의 성능 수준에서 프런티어 출시의 자율 소프트웨어 엔지니어링 역량 진전을 측정하는 데 더 이상 적합하지 않음을 시사합니다.
  current_issues: none


## Top 5 Problem Items

- `why-we-no-longer-evaluate-swe-bench-verified.block-013` | overall=90.6
  evaluated_candidate: 모델은 테스트를 보지 못합니다. 원래 이슈 텍스트와 수정 전 저장소 상태만을 바탕으로 코드 변경을 만들어야 합니다. 코드 변경을 적용한 뒤 모든 테스트가 통과해야만 해당 문제가 해결된 것으로 간주됩니다.
  issues: 의미는 정확하지만 "테스트 코드"가 단순히 "테스트"로 완화되어 약간 덜 구체적입니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-003` | overall=91.5
  evaluated_candidate: 새로운 분석에서 우리는 Verified 세트에 두 가지 주요 문제가 있음을 확인했으며, 이는 이 벤치마크가 오늘날의 성능 수준에서 프런티어 출시의 자율 소프트웨어 엔지니어링 역량 진전을 측정하는 데 더 이상 적합하지 않음을 시사합니다.
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-017` | overall=91.5
  evaluated_candidate: 환경 설정(예: Linux와 Windows의 차이 또는 Python 버전)에 따라 일부 테스트가 오탐으로 실패할 수 있습니다.
  issues: “오탐”은 다소 기술적/축약적 표현입니다., ‘could spuriously fail’는 과거 서술이므로 시제 일관성을 맞추면 더 자연스럽습니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-024` | overall=91.7
  evaluated_candidate: 나머지 5.1%의 작업에는 이 분류 체계로는 잘 묶기 어려운 기타 문제가 있었습니다.
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-012` | overall=91.8
  evaluated_candidate: 수정과 무관한 기능이 손상되지 않고 유지되도록, 수정 전후 모두 통과해야 하는 회귀 테스트
  issues: 원문의 "ensure unrelated functionality remains intact"가 다소 덜 직접적으로 표현됨.

## Terminology Mismatch Examples

- none

## Backtranslation Mismatch Examples

- `why-we-no-longer-evaluate-swe-bench-verified.block-019` | backtranslation_similarity_score=69.1
  evaluated_candidate: 너무 제한적이거나 너무 광범위한 테스트
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-044` | backtranslation_similarity_score=83.8
  evaluated_candidate: 둘째, 자동 채점을 제대로 구현하는 일은 까다롭습니다. 완벽한 테스트 케이스는 올바른 기능을 완전히 검증해야 하며, 중요하지 않은 특정 구현 세부사항에는 구애받지 않으면서도 편법적인 해결책에도 견고해야 합니다. 이러한 문제는 본질적으로 복잡하고 해결하기 어렵습니다. 이런 문제를 찾아내는 데에는 여러 차례에 걸친 대규모 수동 레이블링 작업이 필요했습니다.
  issues: ‘자동 채점’은 원문의 의미를 잘 전달하지만, 문맥상 ‘자동화된 채점’이 더 공식적입니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-017` | backtranslation_similarity_score=84.2
  evaluated_candidate: 환경 설정(예: Linux와 Windows의 차이 또는 Python 버전)에 따라 일부 테스트가 오탐으로 실패할 수 있습니다.
  issues: “오탐”은 다소 기술적/축약적 표현입니다., ‘could spuriously fail’는 과거 서술이므로 시제 일관성을 맞추면 더 자연스럽습니다.
- `why-we-no-longer-evaluate-swe-bench-verified.block-024` | backtranslation_similarity_score=85.2
  evaluated_candidate: 나머지 5.1%의 작업에는 이 분류 체계로는 잘 묶기 어려운 기타 문제가 있었습니다.
  issues: none
- `why-we-no-longer-evaluate-swe-bench-verified.block-014` | backtranslation_similarity_score=85.5
  evaluated_candidate: 이 평가에는 모델의 역량을 과소평가하게 만들 수 있는 여러 문제가 있음을 발견했습니다.
  issues: "could lead to"가 "~할 수 있는"으로 잘 번역되어 의미상 자연스럽습니다.

## Still Needs Human Review

- none
