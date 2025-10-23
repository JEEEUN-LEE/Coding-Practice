/*------------------------------------------------------------*/
/* SAS - 결측치 제거 및 그룹별 합계 구하기 */
/*------------------------------------------------------------*/

/*  데이터 불러오기 */
proc import datafile = '/home/u45061472/basic1.csv'
	out = mydata
	dbms = csv
	replace;
	getnames = yes;
run;

/*------------------------------------------------------------*/
/*  f1 결측치 제거 */
data cleaned_data;
	set mydata;
	where not missing(f1);
run;

/*------------------------------------------------------------*/
/*  city, f2 기준으로 그룹화하여 f1 합계 계산 */
proc summary data = cleaned_data nway;
	class city f2;
	var f1;
	output out = sum_data sum = total_f1;
run;

/*------------------------------------------------------------*/
/*  그룹별 합계 결과 출력 */
proc print data = sum_data;
	title 'Sum of f1 grouped by city and f2';
	var city f2 total_f1;
run;

/*------------------------------------------------------------*/
/*  city='경기' 이고 f2=0 인 조건의 f1 값 출력 */
data filtered_data;
	set mydata;
	if city = '경기' and f2 = 0;
run;

proc print data = filtered_data;
	title 'Values of f1 where city = 경기 and f2 = 0';
	var f1;
run;

/*------------------------------------------------------------*/
/* 주요 개념 요약
   ▪ WHERE NOT MISSING(f1) : f1 컬럼의 결측값 제거
   ▪ PROC SUMMARY : 그룹별 합계, 평균 등 요약 통계 계산 (nway 옵션은 지정된 그룹별로만 요약)
   ▪ CLASS : 그룹 기준 변수 지정
   ▪ OUTPUT OUT= : 요약 결과를 새로운 데이터셋으로 저장
   ▪ PROC PRINT : 결과 테이블 출력
------------------------------------------------------------*/
