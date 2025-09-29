/*데이터 불러오기*/
filename refile 'C:/cars.xlsx';
proc import datafile = refile
	dbms = xlsx
	out = work.car;
	getnames = yes;
run;
proc contents data work.car; run;
/*회귀분석 모델 */
proc reg data = car;
model horsepower = cylinders enginesize / vif;
run;

/*회귀분석 결과 해석
수정된 결정계수 - 조정된 설명력으로 overfitting 가능성 적다고 할 수 있음
f-value, pvalue로 모델이 통계적으로 유의미한지 알 수 있음
rood mse 잔차 크기가 평균에 속하는지 알 수 있음
coeff var 19.04%면 적당한 변동성을 갖고 있다는 것을 알 수 있음

Cylinders 계수 23.70 pvalue <.0001 -> Cylinders 1 증가하면 Horsepower 23.7 증가한다는 것
EngineSize 계수 21.35 pvalue <.0001 -> EngineSize 1 증가하면 21.35 증가한다는 것 
둘 다 유의미한 영향을 미치는 변수

