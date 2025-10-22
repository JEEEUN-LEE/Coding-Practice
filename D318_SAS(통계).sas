/*------------------------------------------------------------*/
/* SAS - 왜도(Skewness)와 첨도(Kurtosis) 분석 */
/*------------------------------------------------------------*/
/* 개념 요약
   ▪ 왜도(Skewness): 분포의 비대칭 정도를 나타내는 지표
      - 오른쪽 꼬리가 길면(+) → 양의 왜도
      - 왼쪽 꼬리가 길면(-) → 음의 왜도
      - 완전 대칭(T분포 등)은 왜도 = 0
   ▪ 첨도(Kurtosis): 분포의 뾰족한 정도를 나타내는 지표
      - 중심에 데이터가 몰려 있으면 뾰족(>3)
      - 고루 퍼져 있으면 평평(<3)
*/

/*------------------------------------------------------------*/
/* ① 데이터 불러오기 */
proc import datafile = '/home/u45061472/train.csv'
	out = mydata
	dbms = csv
	replace;
	getnames = yes;
run;

/*------------------------------------------------------------*/
/* ② 로그 변환 전 왜도·첨도 확인 */
proc means data = mydata n mean std skewness kurtosis;
	var SalePrice;
run;

/*------------------------------------------------------------*/
/* ③ 로그 스케일 변환 (정규성 개선 목적) */
data mydata;
	set mydata;
	Log_SalePrice = log1p(SalePrice); /* log(SalePrice + 1) */
run;

/*------------------------------------------------------------*/
/* ④ 로그 변환 후 왜도·첨도 확인 */
proc means data = mydata n mean std skewness kurtosis;
	var Log_SalePrice;
	output out = stats
		skewness = Skewness
		kurtosis = Kurtosis;
run;

/*------------------------------------------------------------*/
/* ⑤ 왜도와 첨도의 합 계산 */
data stats_sum;
	set stats;
	Sum_Skewness_Kurtosis = Skewness + Kurtosis;
	format Sum_Skewness_Kurtosis 8.2; /* 소수점 둘째 자리까지 표시 */
run;

/*------------------------------------------------------------*/
/* ⑥ 결과 출력 */
proc print data = stats_sum noobs;
	var Skewness Kurtosis Sum_Skewness_Kurtosis;
run;

/*------------------------------------------------------------*/
/* ▪ log1p()는 log(x+1) 계산함
   ▪ 로그 변환은 큰 수를 작은 수로 줄여 정규성이 높아짐
   ▪ 왜도와 첨도를 줄여서 데이터 분석 시 의미있는 결과 도출 가능.
------------------------------------------------------------*/
