# -------------------------------------------------------------
# 선형모델과 신경망 (Linear Model & Neural Network)
# -------------------------------------------------------------

"""
신경망의 기본 구조

- 입력 벡터 (Input Vector): 독립변수
- 출력 벡터 (Target Vector): 종속변수
- 가중치 (Weights): 각 입력에 부여되는 중요도
- 편향 (Bias): 입력값과 상관없이 더해지는 상수항 (절편과 유사)

예시: 꽃받침 길이(sepal length)와 너비(sepal width)로 꽃 종(class)을 예측하는 모델
"""

# -------------------------------------------------------------
# 1. 단순 퍼셉트론 (Single Perceptron)
# -------------------------------------------------------------
"""
단순 퍼셉트론은 입력 벡터에 가중치를 곱하고, 그 결과를 모두 합한 뒤
활성화 함수를 통해 최종 출력을 내는 구조를 가진다.

수식:
    y = f(w1*x1 + w2*x2 + ... + b)

이 출력 y를 실제 값과 비교하여 손실(loss)을 계산하고,
손실이 최소화되도록 가중치 w와 편향 b를 학습한다.
"""

import numpy as np

# 입력 벡터 (예: 꽃받침 길이, 너비)
X = np.array([
    [4.6, 3.1],
    [5.0, 3.6],
    [6.2, 2.9],
    [5.7, 3.8]
])

# 타겟 벡터 (0=Setosa, 1=Versicolor)
y = np.array([0, 0, 1, 1])

# 가중치 및 편향 초기화
np.random.seed(42)
W = np.random.randn(2)
b = np.random.randn()

def perceptron(x):
    """단순 퍼셉트론 출력 계산"""
    linear_sum = np.dot(x, W) + b
    return np.where(linear_sum > 0, 1, 0)

# 예측 결과
y_pred = perceptron(X)
print("예측 결과:", y_pred)

# -------------------------------------------------------------
# 2. 활성화 함수 (Activation Function)
# -------------------------------------------------------------
"""
활성화 함수는 선형 예측값(linear sum)을 비선형 출력으로 변환하는 역할을 한다.

종류:
- Sigmoid: 출력 범위 (0,1), 로지스틱 회귀 등에서 사용
- ReLU (Rectified Linear Unit): 음수는 0, 양수는 그대로 출력
    -> 일반적으로 많이 쓰이는 함수
- tanh: 출력 범위 (-1,1), 중심화된 비선형 함수
"""

import matplotlib.pyplot as plt

# 활성화 함수 정의
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# 시각화
x_vals = np.linspace(-5, 5, 200)
plt.figure(figsize=(8,5))
plt.plot(x_vals, sigmoid(x_vals), label="Sigmoid")
plt.plot(x_vals, relu(x_vals), label="ReLU")
plt.plot(x_vals, tanh(x_vals), label="tanh")
plt.title("활성화 함수 비교")
plt.legend()
plt.grid()
plt.show()

# -------------------------------------------------------------
# 3. 파라미터 최적화 (Optimization)
# -------------------------------------------------------------
"""
신경망의 학습 과정은 ‘가중치와 편향(파라미터)’을 갱신해 손실을 최소화하는 과정이다.
이때 손실함수의 기울기를 이용해 파라미터를 업데이트하는데, 대표적인 방법은 다음과 같다.

1. **SGD (Stochastic Gradient Descent, 확률적 경사 하강법)**  
   - 데이터를 한 번에 한 샘플(또는 작은 배치)씩 사용하여 손실의 기울기를 계산하고 가중치를 갱신.
   - 계산이 빠르고, 지역 최소점(local minima)을 벗어나는 데 유리하다.

2. **Adam (Adaptive Moment Estimation)**  
   - SGD의 단점을 개선한 방법.
   - 학습률을 자동으로 조정(adaptive)하며, 모멘텀(momentum)을 고려해 빠른 수렴을 유도.
   - 현재 딥러닝에서 가장 널리 사용되는 최적화 알고리즘.
"""
import numpy as np

# 입력 (2차원), 은닉층(3개 노드), 출력(1개)
np.random.seed(42)
X = np.random.rand(4, 2)
y = np.array([[1], [0], [1], [0]])

# 가중치 초기화
W1 = np.random.randn(2, 3)  # 입력층 -> 은닉층
b1 = np.zeros((1, 3))
W2 = np.random.randn(3, 1)  # 은닉층 -> 출력층
b2 = np.zeros((1, 1))

# 활성화 함수 (시그모이드)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 순전파 (Feedforward)
z1 = np.dot(X, W1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, W2) + b2
output = sigmoid(z2)

print("입력 데이터:\n", X)
print("예측 출력:\n", output)
