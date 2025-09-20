- 28년 결혼 (3년 뒤)
- 다른 병원 가까운데에 DM 이직 고려

/*SAS BASE에서 제공하는 프로시저*/
APPEND 데이터셋 아래위로 합치기
COMPARE 두개의 데이터군을 비교하여 서로 다른 점을 출력
CORR 각 변수들 상관계수 구함
FREQ 빈도와 구성비, 누적도수와 누적 구성비 구함
IMPORT 엑셀 등 외부 데이터 읽기 
MEANS 기술 통계량 구하기
PLOT 두 변수의 2차원 그래프 그리기
PRINT 자료 프린트 
SORT 자료 정렬(오름, 내림차순)
TRANSPOSE 자료 행과 열을 전치 
SUMMARY, TABULATE, UNIVARIATE 기술통계량 구하기

/*SAS STAT에서 제공하는 프로시저*/
ANOVA 분산분석(세그룹 이상 평균치 차이 검정)
CALIS 선형모형의 공분산분석
CANCORR 정준상관분석
CANDISC 판별분석
DISCRIM 판별분석
FACTOR 요인분석
LIFEREG 생존기간에 대한 회귀모형분석
LOGISTIC 로지스틱반응함수분석
NLIN 비선형회귀분석
PRINCOMP 주성분분석
TTEST T-검정(두 그룹 사이의 평균치 차이 검정
REG 종속변수와 독립변수 간의 선형관계 분석 

PROC REG; MODEL Wei = Hei; /*Wei 가 종속변수, Hei가 독립변수 , 선형모델 */

/*SAS SQL에서 제공하는 프로시저*/
PROC SQL; SELECT * FROM a1;
PROC SQL; SELECT hei, wei FROM a1;
	SELECT gender, MEAN(hei) AS 평균값 FROM a1
	GROUP BY gender;
QUIT;

/* 조인의 종류*/
1) FULL JOIN: 합집합
proc sort data = work.subject_test1_1;
by id;
run;

data work.full_join;
merge work.subject_test1_1 work.phonehw;
by id;
run;

proc print data = work.full_join;
run;

2) INNER JOIN 교집합
3) RIGHT JOIN : 오른쪽 테이블 기준 결합 
data work.rightjoin;
merge work.subject_test1_1(in = emps) work.phonehw2(in = cell);
by id;
if emps = 0 and cell = 1;
run;
4) LEFT JOIN : 왼쪽 테이블 기준으로 결합
즉, a왼쪽테이블은 그대로 두고, B오른쪽 테이블이 A랑 매칭되는게 있으면 그부분 결합하고, 없으면 NULL 값으로 채워진다.

/* FORMAT, INFORMAT*/
INFORMAT은 데이터를 불러올 때 데이터 유형을 변경한다. (외부데이터> 내부저장형식)
FORMAT은 데이터를 불러온 후, 데이터 유형을 변경한다. (내부저장형식> 출력값)
- FORMAT은 숫자/문자/날짜 포맷으로 나뉜다.

