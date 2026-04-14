# Phase 1 Pair Review Worksheet

이 파일은 `why-we-no-longer-evaluate-swe-bench-verified` 쌍의 improved run 기준 human review queue입니다.

- 목적: 자동 승격이 아니라, 유지보수자가 직접 확인할 블록만 추려서 검토합니다.
- 선택 기준: improved eval 기준 낮은 overall score, 남아 있는 issue, 낮은 backtranslation score를 함께 고려했습니다.
- 상태: 아래 모든 항목의 `decision`은 `pending_human_review`입니다. 승인 전에는 어떤 항목도 `reviewed_golden`이 아닙니다.
- `reviewed_golden_ko (draft)`: 현재 `improved_candidate_ko`를 임시 초안으로 넣었습니다. 유지보수자가 그대로 승인하거나 수정해야 합니다.

## why-we-no-longer-evaluate-swe-bench-verified.block-013

- decision: `pending_human_review`
- overall_score: `90.6`
- semantic_similarity_score: `79.8`
- backtranslation_similarity_score: `90.1`

### source_en

The model does not see the tests. It has to produce a code change given only the original issue text and the state of the repository before the fix. It passes a problem only if all tests pass after the code change is applied.

### reference_ko

모델에게는 이 테스트 코드가 제공되지 않습니다. 원본 이슈 텍스트와 수정 전 리포지터리 상태만 주어진 환경에서 코드 수정안을 생성해야 합니다. 코드 변경 사항이 적용된 후 모든 테스트를 통과해야만 해당 문제를 통과한 것으로 간주됩니다.

### candidate_ko

모델은 테스트를 보지 못합니다. 원래 이슈 텍스트와 수정 전 저장소의 상태만을 바탕으로 코드 변경을 만들어야 합니다. 코드 변경을 적용한 뒤 모든 테스트가 통과해야만 해당 문제를 해결한 것으로 간주됩니다.

### improved_candidate_ko

모델은 테스트를 보지 못합니다. 원래 이슈 텍스트와 수정 전 저장소 상태만을 바탕으로 코드 변경을 만들어야 합니다. 코드 변경을 적용한 뒤 모든 테스트가 통과해야만 해당 문제가 해결된 것으로 간주됩니다.

### reviewed_golden_ko (draft)

모델은 테스트를 보지 못합니다. 원래 이슈 텍스트와 수정 전 저장소 상태만을 바탕으로 코드 변경을 만들어야 합니다. 코드 변경을 적용한 뒤 모든 테스트가 통과해야만 해당 문제가 해결된 것으로 간주됩니다.

### notes

- 의미는 정확하지만 `"테스트 코드"`가 단순히 `"테스트"`로 완화되어 약간 덜 구체적입니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-003

- decision: `pending_human_review`
- overall_score: `91.5`
- semantic_similarity_score: `84.8`
- backtranslation_similarity_score: `90.4`

### source_en

In a new analysis, we found two major issues with the Verified set that indicate the benchmark is no longer suitable for measuring progress on autonomous software engineering capabilities for frontier launches at today’s performance levels:

### reference_ko

새로운 분석 결과, Verified 데이터세트에서 두 가지 주요 문제를 발견했습니다. 이는 현재의 성능 수준에서 프런티어 모델 출시에 수반되는 자율 소프트웨어 엔지니어링 역량 발전을 측정하는 데 해당 벤치마크가 더 이상 적합하지 않음을 시사합니다.

### candidate_ko

새로운 분석에서 우리는 Verified 세트에 두 가지 주요 문제가 있음을 확인했으며, 이는 이 벤치마크가 더 이상 오늘날의 성능 수준에서 최첨단 출시를 위한 자율 소프트웨어 엔지니어링 역량의 진전을 측정하는 데 적합하지 않음을 시사합니다:

### improved_candidate_ko

새로운 분석에서 우리는 Verified 세트에 두 가지 주요 문제가 있음을 확인했으며, 이는 이 벤치마크가 오늘날의 성능 수준에서 프런티어 출시의 자율 소프트웨어 엔지니어링 역량 진전을 측정하는 데 더 이상 적합하지 않음을 시사합니다.

### reviewed_golden_ko (draft)

새로운 분석에서 우리는 Verified 세트에 두 가지 주요 문제가 있음을 확인했으며, 이는 이 벤치마크가 오늘날의 성능 수준에서 프런티어 출시의 자율 소프트웨어 엔지니어링 역량 진전을 측정하는 데 더 이상 적합하지 않음을 시사합니다.

### notes

- 자동 issue 문구는 없지만 score가 낮은 편이고, `"frontier launches"` 처리와 문장 리듬이 official style과 맞는지 확인이 필요합니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-017

- decision: `pending_human_review`
- overall_score: `91.5`
- semantic_similarity_score: `91.0`
- backtranslation_similarity_score: `84.2`

### source_en

Depending on setup of the environment (for example Linux vs Windows, or the python version), some tests could spuriously fail

### reference_ko

환경 설정(예: Linux와 Windows의 차이, 또는 Python 버전)에 따라 일부 테스트가 실제 오류가 없는데도 실패할 수 있었습니다.

### candidate_ko

환경 설정에 따라(예: Linux vs Windows, 또는 python 버전) 일부 테스트가 우연히 실패할 수 있습니다

### improved_candidate_ko

환경 설정(예: Linux와 Windows의 차이 또는 Python 버전)에 따라 일부 테스트가 오탐으로 실패할 수 있습니다.

### reviewed_golden_ko (draft)

환경 설정(예: Linux와 Windows의 차이 또는 Python 버전)에 따라 일부 테스트가 오탐으로 실패할 수 있습니다.

### notes

- `"오탐"`은 다소 기술적이고 축약적인 표현입니다.
- `could spuriously fail`는 과거 서술이므로 시제 일관성을 맞추면 더 자연스럽습니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-024

- decision: `pending_human_review`
- overall_score: `91.7`
- semantic_similarity_score: `86.7`
- backtranslation_similarity_score: `85.2`

### source_en

The remaining 5.1% of tasks had miscellaneous issues that were not well grouped with this taxonomy.

### reference_ko

나머지 5.1%의 작업에는 이 분류 기준에 명확하게 속하지 않는 기타 문제가 있었습니다.

### candidate_ko

나머지 5.1%의 작업에는 이 분류 체계로는 잘 묶이지 않는 기타 문제가 있었습니다.

### improved_candidate_ko

나머지 5.1%의 작업에는 이 분류 체계로는 잘 묶기 어려운 기타 문제가 있었습니다.

### reviewed_golden_ko (draft)

나머지 5.1%의 작업에는 이 분류 체계로는 잘 묶기 어려운 기타 문제가 있었습니다.

### notes

- 자동 issue 문구는 없지만 semantic/backtranslation score가 모두 낮은 편이라 표현 선택을 직접 확인하는 편이 안전합니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-012

- decision: `pending_human_review`
- overall_score: `91.8`
- semantic_similarity_score: `81.1`
- backtranslation_similarity_score: `94.7`

### source_en

Regression tests that pass both before and after the fix to ensure unrelated functionality remains intact.

### reference_ko

버그 수정과 무관한 기존 기능이 손상되지 않고 유지됨을 보장하기 위해, 수정 전후에 모두 통과해야 하는 회귀 테스트

### candidate_ko

수정 전과 후 모두 통과하여, 관련 없는 기능이 그대로 유지되는지 확인하는 회귀 테스트

### improved_candidate_ko

수정과 무관한 기능이 손상되지 않고 유지되도록, 수정 전후 모두 통과해야 하는 회귀 테스트

### reviewed_golden_ko (draft)

수정과 무관한 기능이 손상되지 않고 유지되도록, 수정 전후 모두 통과해야 하는 회귀 테스트

### notes

- 원문의 `"ensure unrelated functionality remains intact"`가 여전히 다소 압축되어 표현됩니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-019

- decision: `pending_human_review`
- overall_score: `92.3`
- semantic_similarity_score: `100.0`
- backtranslation_similarity_score: `69.1`

### source_en

Too narrow and too wide tests

### reference_ko

너무 제한적이거나 너무 광범위한 테스트

### candidate_ko

너무 좁고 너무 넓은 테스트

### improved_candidate_ko

너무 제한적이거나 너무 광범위한 테스트

### reviewed_golden_ko (draft)

너무 제한적이거나 너무 광범위한 테스트

### notes

- 문장 자체는 자연스럽지만 backtranslation score가 유난히 낮아서 다시 한 번 확인 대상으로 남깁니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-015

- decision: `pending_human_review`
- overall_score: `93.1`
- semantic_similarity_score: `86.7`
- backtranslation_similarity_score: `94.3`

### source_en

Some unit tests were overly specific or misaligned with the task so correct fixes could be rejected.

### reference_ko

일부 단위 테스트는 지나치게 구체적이거나 작업 목적과 어긋나 있어, 올바른 수정안마저 거부될 수 있었습니다.

### candidate_ko

일부 단위 테스트는 지나치게 구체적이거나 과제와 맞지 않아, 올바른 수정도 거부될 수 있었습니다.

### improved_candidate_ko

일부 단위 테스트는 지나치게 구체적이거나 과제와 맞지 않아, 올바른 수정도 거부될 수 있었습니다.

### reviewed_golden_ko (draft)

일부 단위 테스트는 지나치게 구체적이거나 과제와 맞지 않아, 올바른 수정도 거부될 수 있었습니다.

### notes

- `"task"`를 `"과제"`로 옮긴 선택이 무난하지만, 문맥상 `"작업"`도 가능한지 확인이 필요합니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.

## why-we-no-longer-evaluate-swe-bench-verified.block-040

- decision: `pending_human_review`
- overall_score: `93.7`
- semantic_similarity_score: `99.7`
- backtranslation_similarity_score: `89.6`

### source_en

Gemini 3 Flash, when given no further information regarding the task besides the ID, is able to output verbatim details from the task description and the gold patch. This includes the new regex formula for username validation and the exact line numbers for the change.

### reference_ko

Gemini 3 Flash는 작업 ID 외에 작업에 대한 추가 정보가 주어지지 않았음에도, 작업 설명과 골드 패치의 세부 내용을 글자 그대로 출력할 수 있습니다. 여기에는 사용자 이름 유효성 검사를 위한 새로운 정규식과 변경 사항의 정확한 줄 번호가 포함됩니다.

### candidate_ko

Gemini 3 Flash는 과제 ID 외에 추가 정보가 전혀 주어지지 않아도, 과제 설명과 골드 패치의 세부 사항을 그대로 출력할 수 있습니다. 여기에는 사용자 이름 검증을 위한 새 regex 수식과 변경된 정확한 줄 번호가 포함됩니다.

### improved_candidate_ko

Gemini 3 Flash는 작업 ID 외에 작업에 대한 추가 정보가 전혀 주어지지 않아도, 작업 설명과 골드 패치의 세부 내용을 글자 그대로 출력할 수 있습니다. 여기에는 사용자 이름 유효성 검사를 위한 새로운 정규식과 변경 사항의 정확한 줄 번호가 포함됩니다.

### reviewed_golden_ko (draft)

Gemini 3 Flash는 작업 ID 외에 작업에 대한 추가 정보가 전혀 주어지지 않아도, 작업 설명과 골드 패치의 세부 내용을 글자 그대로 출력할 수 있습니다. 여기에는 사용자 이름 유효성 검사를 위한 새로운 정규식과 변경 사항의 정확한 줄 번호가 포함됩니다.

### notes

- `"regex 수식"`은 improved 단계에서 정리됐지만, `"골드 패치"`와 `"작업 ID"` 표현이 최종 publication tone에 맞는지 한 번 더 확인하는 편이 좋습니다.
- Maintainer confirmation required before any promotion to `reviewed_golden`.
