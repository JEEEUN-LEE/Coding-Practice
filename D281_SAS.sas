SAS 비번 wldms@439000

# CONTENTS 프로시저
데이터셋에 대한 정보를 출력하는 정보
# FORMAT 프로시저
변수의 값과 레이블을 설정하는 프로시저
# PRINT 프로시저
데이터셋에 대한 값을 출력하는 프로시저
# SORT 프로시저
입력한 변수에 대해 오름차순으로 정렬
DATA score;
	INFILE tempurl dlm = ' ' FIRSTOBS = 2;
	INPUT dept $ grade $ mid final report avg;
RUN; 

/*데이터 확인*/
PROC PRINT DATA = score;
RUN;

/* 중간, 기말, 보고서, 평균 점수에 대한 기초 통계량 계산 */
PROC MEANS DATA= score N MEAN MEDIAN STD MIN MAX;
	VAR mid final report avg;
	FORMAT mid final report avg 7.4;
RUN;

/* 파일닫기*/
FILENAME tempurl CLEAR;

/*자료 분석하기*/
PROC MEANS; VAR hei wei age; /*변수 hei, wei, age의 평균값 등 기술 통계량을 구한다*/
PROC REG; MODEL wei = hei; /*종속변수 wei, 독립변수 hei로 하는 회귀g방정식을 구한다 */
bmi = wei / (hei/100) **2; /*bmi 구하기*/
