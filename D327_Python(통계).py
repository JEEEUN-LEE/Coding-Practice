# ============================================================
# 일반선형모델(GLM) - Deviance, 우도비검정, 푸아송 회귀
# ============================================================

import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import statsmodels.formula.api as smf
import statsmodels.api as sm

# ============================================================
# 1. Deviance와 우도비 검정
# ============================================================

# Deviance는 모델의 적합도를 평가하는 지표로,
# 로그우도 차이에 2를 곱한 값이다.
# 이는 두 모델 간 우도비 검정(Likelihood Ratio Test, LRT)에 사용하기 편하도록 만든 형태이다.

# 즉, "Deviance 차이를 검정"하는 것이 곧 "우도비 검정"이다.

# 예시: 로지스틱 회귀모델
test_result = pd.read_csv('../data/test_result.csv')
mod_glm = smf.glm("result ~ hours", data=test_result, family=sm.families.Binomial()).fit()

# 예측 성공확률
pred = mod_glm.predict()
y = test_result["result"]

# --------------------------------------------
# Deviance 잔차 계산
# --------------------------------------------
# deviance_resid = sqrt(2 * (log-likelihood 차이)) * sign(y - μ)

resid_tmp = 0 - np.log(sp.stats.binom.pmf(k=y, n=1, p=pred))
deviance_resid = np.sqrt(2 * resid_tmp) * np.sign(y - pred)

print("\n[Deviance Residuals - 상위 3개]")
print(deviance_resid.head(3))

# 합격여부를 완전히 예측할 수 있는 경우 log(1)=0이 되므로 deviance는 항상 0이다.


# ============================================================
# 2. 교차 엔트로피(Cross Entropy)와의 관계
# ============================================================

# 이항분포의 확률질량함수는 다음과 같다:
#   f(y) = p^y * (1-p)^(1-y)
# 이를 로그변환하면 로그우도(log-likelihood)가 된다.

# 교차엔트로피는 다음과 같이 정의된다:
#   - [ y*log(p) + (1-y)*log(1-p) ]
#
# 따라서 교차엔트로피를 최소화하는 것은
# deviance를 최소화하는 것과 동일하며,
# 이는 로지스틱 회귀에서 로그우도를 최대로 하는 것과 같다.

# 즉, 
# "교차엔트로피 오차 최소화 ↔ deviance 최소화 ↔ 로그우도 최대화"
# 세 가지는 같은 의미를 가진다.


# ============================================================
# 3. 푸아송 회귀 (Poisson Regression)
# ============================================================

# 푸아송 회귀는 사건 발생 횟수(Count Data)를 분석할 때 사용한다.
# 종속변수 Y ~ Poisson(μ)
# 링크함수: log(μ) = Xβ
#
# 평균과 분산이 같다는 가정이 있으며,
# 관찰 단위(예: 시간, 인원, 기간)에 대한 '노출시간 보정'이 필요하다.

# 예시: 입원기간, 나이, 치료 여부가 감염건수에 미치는 영향 분석

# 예시용 가상 데이터
data = pd.DataFrame({
    'events': [3, 1, 4, 0, 2, 5, 1, 0],
    'days': [10, 8, 12, 9, 10, 15, 7, 8],
    'age': [50, 40, 70, 60, 55, 80, 45, 35],
    'treatment': [1, 0, 1, 1, 0, 0, 1, 0]
})

# 로그(관찰기간) 보정
data['log_days'] = np.log(data['days'])

# 포아송 회귀모델 적합
model = smf.glm(
    formula='events ~ age + treatment',
    data=data,
    family=sm.families.Poisson(),
    offset=data['log_days']
).fit()

print("\n[Poisson Regression Summary]")
print(model.summary())

# --------------------------------------------
# 계수 해석
# --------------------------------------------
# exp(계수) = 사건 발생비율(Rate Ratio)
# 예: exp(treatment 계수) < 1 → 치료군의 사건 발생률이 낮다.

rate_ratio = np.exp(model.params)
print("\n[발생비율(Rate Ratio)]")
print(rate_ratio)

# 예시 해석:
# 치료군의 exp(계수)=0.67 → 대조군 대비 33% 낮은 발생률
# 고령(age)일수록 감염위험 증가


# ============================================================
# 4. 푸아송 회귀의 수학적 구조
# ============================================================

# 링크함수: log(μ) = β0 + β1 * x
# → 양변에 exp를 취하면 μ = exp(β0 + β1 * x)
#
# 따라서 종속변수가 음수가 되지 않고,
# ‘기온 vs 판매개수’, ‘시간 vs 방문수’ 같은 카운트 데이터에 적합하다.


# ============================================================
# 5. 푸아송 회귀 실습 예시
# ============================================================

# 가상의 맥주 판매 데이터 예시
beer = pd.DataFrame({
    'beer_number': [20, 25, 40, 45, 60, 70, 80],
    'temperature': [15, 17, 20, 22, 25, 28, 30]
})

# 모델 적합
mod_pois = smf.glm('beer_number ~ temperature', data=beer, family=sm.families.Poisson()).fit()
print("\n[Beer Sales Poisson Regression Summary]")
print(mod_pois.summary())

# 기온의 계수가 양수 → 기온이 오를수록 맥주 판매 개수 증가
# AIC 비교 시, 독립변수를 추가한 모델의 AIC가 더 작다면 해당 변수는 유의미하다.

# 로그링크 사용 시 해석:
# 일반 회귀: "기온이 1도 오르면 매출이 X원 증가"
# 로그 회귀: "기온이 1도 오르면 매출이 Y배 증가"
# (덧셈 관계가 로그 취하면 곱셈 관계로 변환됨)
