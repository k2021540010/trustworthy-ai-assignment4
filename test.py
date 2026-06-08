"""
test.py - α,β-CROWN을 사용한 Iris 모델 robustness 검증 데모
"""
import os
import sys
import subprocess
import time

# 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ABCROWN_DIR = os.path.join(BASE_DIR, "alpha-beta-CROWN", "complete_verifier")
CONFIG_PATH = os.path.join(BASE_DIR, "iris_verification.yaml")

def main():
    print("=" * 60)
    print("  α,β-CROWN 신경망 검증 데모")
    print("  모델: Iris FC Network (4 → 8 → 16 → 3)")
    print("  검증 속성: ε=0.01 (ℓ∞-ball) robustness")
    print("=" * 60)

    print(f"\n[1] 모델 경로: {os.path.join(BASE_DIR, 'iris_model.onnx')}")
    print(f"[2] Config 경로: {CONFIG_PATH}")
    print(f"[3] VNNLib 경로: {os.path.join(BASE_DIR, 'iris_property.vnnlib')}")
    print("\n[4] α,β-CROWN 실행 중...\n")

    start = time.time()

    result = subprocess.run(
        [sys.executable, "abcrown.py", "--config", CONFIG_PATH],
        cwd=ABCROWN_DIR,
        capture_output=False
    )

    elapsed = time.time() - start

    print("\n" + "=" * 60)
    print(f"[5] 검증 완료 (총 소요 시간: {elapsed:.2f}초)")
    print("=" * 60)

if __name__ == "__main__":
    main()
