# Trustworthy AI Assignment 4 - α,β-CROWN Neural Network Verification

## 개요
α,β-CROWN을 사용하여 Iris 데이터셋으로 학습한 FC 네트워크의 robustness를 형식적으로 검증합니다.

- **검증 모델**: Iris FC Network (4 → 8 → 16 → 3)
- **검증 속성**: ε=0.01 (ℓ∞-ball) 범위 내 robustness
- **검증 결과**: unsat (검증 성공, 0.49초)

---

## 환경 설정

### 1. 레포지토리 클론
    git clone https://github.com/k2021540010/trustworthy-ai-assignment4.git
    cd trustworthy-ai-assignment4

### 2. α,β-CROWN 서브모듈 초기화
    git submodule update --init --recursive

### 3. conda 환경 생성 및 활성화
    conda env create -f environment.yml
    conda activate abcrown

### 4. auto_LiRPA 설치
    cd alpha-beta-CROWN
    pip install -e .
    cd ..

---

## 파일 구조

    trustworthy-ai-assignment4/
    ├── alpha-beta-CROWN/       # α,β-CROWN 서브모듈
    ├── iris_model.onnx         # 검증할 Iris FC 모델 (ONNX 형식)
    ├── iris_property.vnnlib    # 검증 속성 (VNNLib 형식)
    ├── iris_verification.yaml  # α,β-CROWN 설정 파일
    ├── generate_vnnlib.py      # VNNLib 파일 생성 스크립트
    ├── test.py                 # 검증 실행 데모
    ├── environment.yml         # conda 환경 파일
    └── README.md

---

## 실행 방법

    python3 test.py

---

## 결과 요약

| 항목 | 내용 |
|------|------|
| 모델 | Iris FC Network (4→8→16→3) |
| 데이터셋 | Iris (클래스 0 샘플) |
| 검증 속성 | ℓ∞-ball, ε=0.01 |
| 결과 | unsat (robustness 검증 성공) |
| 소요 시간 | 0.49초 |

---

## Marabou vs α,β-CROWN 비교

| 항목 | Marabou (Assignment 3) | α,β-CROWN (Assignment 4) |
|------|----------------------|--------------------------|
| 결과 | sat (반례 발견) | unsat (검증 성공) |
| 시간 | ~24ms | ~0.49초 |
| 방식 | SMT solver | Linear relaxation + BnB |
| 설정 방식 | Python API | YAML + VNNLib |