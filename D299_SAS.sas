/* SAS  */
proc reg data = car;
model horsepower = cylinders weight wheelbase legnth / vif 
run;
/*ANOVA 모델
R-Square 0.6743 -> 전체 변동성의 67.4% 설명
F-Statistic의 P-value <0.0001로 회귀모델은 통계적으로 유의미함
VIF 다중공선성 지표 10 미만이면 OK, 높으면 변수 변환 등의 방법을 사용할 수 있음 */
/* 잔차분석 
잔차가 대체로 수평하게 분포해서 선형성 가정은 대체로 만족하는 경향이 있다: QQ플롯(정규성)
중간부분은 직선에 잘 맞지만 양 끝 부분에서 약간 벗어나는 모습: Cook's Distance
일부 관측치가 다른 데이터에 비해 영향력이 큰 것으로 보임 
대체로 정규분포 형태를 따르나 약간의 비대칭성 존재*/