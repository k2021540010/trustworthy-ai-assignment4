import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

iris = load_iris()
X = iris.data.astype(np.float32)
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

sample = X[0]
label = 0
epsilon = 0.01
n_inputs = 4
n_outputs = 3

lines = []

for i in range(n_inputs):
    lines.append(f"(declare-const X_{i} Real)")

for i in range(n_outputs):
    lines.append(f"(declare-const Y_{i} Real)")

lines.append("")

lines.append("; 입력 제약: epsilon=0.01 범위")
for i in range(n_inputs):
    lb = float(sample[i]) - epsilon
    ub = float(sample[i]) + epsilon
    lb = max(0.0, lb)
    ub = min(1.0, ub)
    lines.append(f"(assert (>= X_{i} {lb:.6f}))")
    lines.append(f"(assert (<= X_{i} {ub:.6f}))")

lines.append("")

lines.append("; 출력 제약: 클래스 0이 아닌 다른 클래스가 더 크면 falsified")
for j in range(n_outputs):
    if j != label:
        lines.append(f"(assert (>= Y_{j} Y_{label}))")

with open("iris_property.vnnlib", "w") as f:
    f.write("\n".join(lines))

print("iris_property.vnnlib 생성 완료!")
print(f"샘플: {sample}")
print(f"epsilon: {epsilon}")
