/*회귀분석 해석*/
/* nOuts 절편 395.16-> nOuts이 0일 때, salary는 395.16 값을 가진다
  nOuts 기울기 0.48-> nOuts가 1 증가할 때, salary는 0.48만큼 증가
  nOuts p-value <0.001로 nOuts가 salary에 유의미한 양의 영향을 준다고 해석할 수 있음.*/

/* 다중 회귀분석 */
proc reg data = baseball;
model salary = nHone nHits nRuns nOuts nError;
run;

/*다중 회귀분석 결과 해석*/
/* 수정된 R결정계수 0.401 -> 모델이 변동의 약 40.1% 설명할 수 있음
   평균오차크기 355 -> R2이 0.4인건 중간정도 설명력
   회귀계수 salary에 유의미한 영향을 주는 변수인지 확인 가능 */