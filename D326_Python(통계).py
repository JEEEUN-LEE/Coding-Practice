# ===========================================
# 일반 선형모델(GLM) 평가 - 피어슨 잔차와 Deviance
# ===========================================

# -------------------------------------------
# 1. 패키지 불러오기
# -------------------------------------------

import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats

from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

import statsmodels.formula.api as smf
import statsmodels.api as sm

# -------------------------------------------
# 2. 분석 개요
# -------------------------------------------
# 일반선형모델(GLM, Generalized Linear Model)은 종속변수의 분포가
# 정규분포가 아닐 때(예: 이항, 포아송 등) 사용하는 모델이다.
#
# - 모집단 분포가 정규분포 이외인 경우, 잔차 처리 방식이 달라진다.
# - GLM의 적합도 평가는 잔차와 deviance로 수행한다.

# -------------------------------------------
# 3. 데이터 불러오기
# -------------------------------------------

# 예시 데이터 불러오기 (상대 경로 기준)
# test_result.csv 파일은 'hours' (공부시간)과 'result' (합격여부: 0/1) 컬럼을 포함
test_result = pd.read_csv('../data/test_result.csv')

# -------------------------------------------
# 4. GLM 모델링
# -------------------------------------------

# Binomial(이항분포) 로지스틱 회귀 모델
mod_glm = smf.glm(
    formula="result ~ hours",
    data=test_result,
    family=sm.families.Binomial()
).fit()

# 모델 요약 확인
print(mod_glm.summary())

# -------------------------------------------
# 5. 피어슨 잔차 (Pearson Residual)
# -------------------------------------------

# 피어슨 잔차 공식:
# r_i = (y_i - μ_i) / sqrt(V(μ_i))
# 여기서 V(μ_i)는 분산 함수로, 이항분포에서는 μ_i * (1 - μ_i)

pred = mod_glm.predict()              # 예측값 (μ_i)
y = test_result["result"]             # 실제값 (y_i)
pearson_resid = (y - pred) / np.sqrt(pred * (1 - pred))

print("\n[피어슨 잔차 상위 3개]")
print(pearson_resid.head(3))

# -------------------------------------------
# 6. Deviance
# -------------------------------------------

# Deviance는 모델 적합도를 평가하는 지표로,
# 모델이 데이터에 잘 맞지 않으면 값이 커진다.

deviance = mod_glm.deviance
null_deviance = mod_glm.null_deviance

print(f"\n모델 Deviance: {deviance:.3f}")
print(f"Null Deviance: {null_deviance:.3f}")

# Deviance가 줄어들수록 (Null Deviance 대비) 모델의 적합도가 향상된 것이다.