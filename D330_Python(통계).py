# -------------------------------------------------------------
# Hyperparameter Optimization (Tuning)
# -------------------------------------------------------------

"""
parameter vs hyperparameter

- parameter:
  모델 내부에서 학습을 통해 자동으로 조정되는 값들
  (예: 선형회귀의 가중치 W, 절편 b)

- hyperparameter:
  사용자가 직접 설정해야 하는 값들로,
  모델의 구조나 학습 과정에 영향을 주는 요소들
  예: 
    - RandomForest: n_estimators (트리 개수), max_depth (트리 깊이)
    - Neural Network: learning_rate, batch_size, epochs, layer 개수 등
"""

# -------------------------------------------------------------
# 1. Grid Search (그리드 탐색)
# -------------------------------------------------------------
"""
- 사전에 정의한 하이퍼파라미터 후보 값들을 격자(grid) 형태로 조합하여
  모든 조합을 탐색하는 방법.
- 단점: 계산량이 많고, 탐색 공간이 넓을 경우 비효율적.
- 장점: 전수 탐색으로 최적 조합을 확실하게 찾을 수 있음.
"""

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# 데이터 불러오기
X, y = load_iris(return_X_y=True)

# 모델 정의
model = RandomForestClassifier(random_state=42)

# 탐색할 하이퍼파라미터 설정
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10]
}

# Grid Search 실행
grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy')
grid_search.fit(X, y)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)


# -------------------------------------------------------------
# 2. Random Search (랜덤 탐색)
# -------------------------------------------------------------
"""
- 탐색 공간 내에서 임의의 하이퍼파라미터 조합을 랜덤하게 선택하여 평가.
- 전수 탐색보다 빠르며, 탐색 공간이 넓을 때 효율적.
"""

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

# 랜덤 탐색용 분포 설정
param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 15)
}

# Random Search 실행
random_search = RandomizedSearchCV(model, param_distributions=param_dist, 
                                   n_iter=10, cv=3, scoring='accuracy', random_state=42)
random_search.fit(X, y)

print("Best Parameters (Random Search):", random_search.best_params_)
print("Best Score (Random Search):", random_search.best_score_)


# -------------------------------------------------------------
# 3. Bayesian Optimization (베이지안 최적화)
# -------------------------------------------------------------
"""
- 이전의 탐색 결과를 기반으로, 다음 탐색할 하이퍼파라미터 영역을 확률적으로 예측.
- 적은 횟수로도 효율적으로 최적값에 접근 가능.
- 탐색 공간이 복잡하거나 계산 비용이 클 때 효과적.
"""

# 예시: scikit-optimize의 BayesSearchCV 사용
# pip install scikit-optimize 필요

from skopt import BayesSearchCV

# 베이지안 탐색 실행
bayes_search = BayesSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    search_spaces={
        'n_estimators': (50, 300),
        'max_depth': (3, 15)
    },
    n_iter=20,
    cv=3,
    scoring='accuracy',
    random_state=42
)

bayes_search.fit(X, y)
print("Best Parameters (Bayesian):", bayes_search.best_params_)
print("Best Score (Bayesian):", bayes_search.best_score_)
