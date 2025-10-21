/*SAS- 결측치 처리 후 대체*/
/*F1 컬럼에 결측치를 median 값으로 대체하고, city 그룹 별로 F1 컬럼의 평균값을 구하기*/
/* ① 데이터 불러오기 */
proc import datafile = '/home/u45061472/basic1.csv' 
	out = basic
	dbms = csv replace;
	getnames = yes; /* 첫 행을 변수명으로 사용 */
run;

/* ② F1 변수의 중앙값 계산 */
proc means data = basic noprint;
	var f1;
	output out = median_f1 median = median_f1; /* 중앙값을 median_f1 변수에 저장 */
run;

/* ③ 결측치(Missing Value) 처리 */
data basic;
	if _n_ = 1 then set median_f1; /* 중앙값 데이터 병합 */
	if missing(f1) then f1 = median_f1; /* 결측치면 중앙값으로 대체 */
	drop median_f1; /* 중앙값 변수 삭제 (불필요하므로) */
run;

/* ④ 결측치 처리 후 F1 평균값 확인 */
proc means data = basic mean;
	var f1;
run;

/*------------------------------------------------------------*/