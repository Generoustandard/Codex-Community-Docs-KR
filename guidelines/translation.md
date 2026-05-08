# 번역 가이드

## 목적

이 가이드는 공식 OpenAI 영어-한국어 페이지 쌍을 기준으로 한국어 번역 후보를 검토할 때 사용하는 최소 기준입니다.

현재 Phase 1에서는 Developer 문서 예시를 평가 대상으로 쓰지 않습니다. 평가와 검토는 공식 `openai.com` 영문 원문과 공식 한국어 reference를 기준으로 진행합니다.

## 기본 원칙

- 원문 의미를 우선합니다.
- 한국어 문장은 자연스럽게 다듬되, 사실관계와 기술적 제약을 바꾸지 않습니다.
- 제품명, 모델명, 벤치마크명, 코드, 숫자, 고유명사는 임의로 번역하지 않습니다.
- 제목, 링크, 목록, 코드 블록 같은 Markdown 구조는 유지합니다.
- 확신이 없는 해석은 임의로 확정하지 말고 review note에 남깁니다.

## 검토 기준

### 1. 의미 보존

- 원문의 주장, 조건, 제한, 경고를 누락하지 않습니다.
- 한국어가 더 자연스럽더라도 원문 의미가 달라지면 수정 대상입니다.

### 2. 고유명사 유지

다음 항목은 원문 표기를 우선 유지합니다.

- OpenAI
- SWE-bench Verified
- benchmark
- model
- evals
- 숫자, 버전, 날짜

### 3. 한국어 문장 품질

- 영어 어순을 그대로 따라가지 않습니다.
- 긴 문장은 필요하면 나눕니다.
- 과도한 의역이나 설명 추가는 피합니다.
- 같은 문서 안에서는 같은 용어를 반복해서 사용합니다.

### 4. 애매한 부분 처리

- 원문 의미가 모호하면 `reviews/phase1_pair_review.md`의 notes에 남깁니다.
- `candidate_ko`나 `improved_candidate_ko`가 좋아 보여도 human review 전에는 golden으로 취급하지 않습니다.

## 예시

- "SWE-bench Verified became saturated." -> "SWE-bench Verified가 포화 상태에 도달했습니다."
- "We no longer evaluate on this benchmark." -> "이제 이 벤치마크로는 평가하지 않습니다."

## PR 체크리스트

- 원문 의미가 빠지거나 바뀐 부분이 없는가
- 용어 선택이 `guidelines/terminology.md`와 일관되는가
- Markdown 구조, 링크, 코드 블록이 유지되었는가
- 원문 URL과 검토 대상 파일이 PR 설명에 포함되었는가
- 확신이 없는 표현이 review note에 남아 있는가
