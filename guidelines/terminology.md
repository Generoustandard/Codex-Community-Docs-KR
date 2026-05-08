# 용어 가이드

## 기본 방침

- 같은 문서 안에서는 같은 영어 용어를 가능한 한 같은 한국어 표현으로 번역합니다.
- 공식 이름, 제품명, 모델명, 벤치마크명은 원문 표기를 우선 유지합니다.
- 과도한 직역보다 한국어 독자가 이해하기 쉬운 표현을 우선합니다.
- 용어 선택에 확신이 없으면 PR 설명이나 review note에 근거를 남깁니다.

## 시작 용어집

| English term | 권장 한국어 | 메모 |
| --- | --- | --- |
| model | 모델 | 모델 ID는 원문 유지 |
| benchmark | 벤치마크 | 고유 벤치마크명은 원문 유지 |
| evaluation / eval | 평가 | 문맥상 `evals`는 원문 유지 가능 |
| verified | 검증된 / Verified | 고유명사 일부이면 원문 유지 |
| saturation | 포화 | 벤치마크 성능 포화 문맥 |
| candidate | 후보 | `candidate_ko`는 원문 필드명 유지 |
| reference | reference / 기준 번역 | `reference_ko`는 공식 한국어 reference |
| golden | golden / 검토 완료 예시 | 자동 생성물이 아니라 human-reviewed 대상만 해당 |
| backtranslation | 역번역 | 평가 방식 설명에서 사용 |
| cosine similarity | 코사인 유사도 | 평가 지표명 |
| prompt | 프롬프트 | 비교 실험 문맥 |
| pipeline | 파이프라인 | 비교 실험 문맥 |

## 운영 원칙

- `reference_ko`는 공식 한국어 reference이지 자동으로 golden이 아닙니다.
- `candidate_ko`와 `improved_candidate_ko`는 모델 출력이므로 human review 전에는 golden이 아닙니다.
- `reviewed_golden`은 유지보수자 또는 커뮤니티 리뷰어가 승인한 소수 예시만 의미합니다.
- Phase 1에서는 공식 `openai.com` 영문/한국어 페이지 쌍을 기준으로 용어를 맞춥니다.
