/*------------------------------------------------------------*/
/* SAS - PROC UNIVARIATE 활용 예제 */
/*------------------------------------------------------------*/

/* 목적: 단일(수치형) 변수의 분포, 요약통계, 정규성 검정 등을 수행 */
/* 특징:
   ▪ 평균, 중앙값, 분산, 표준편차, 사분위수 등 요약통계 제공
   ▪ 왜도(Skewness), 첨도(Kurtosis) 확인 가능
   ▪ 정규성 검정(Shapiro-Wilk, Kolmogorov-Smirnov 등)
   ▪ 히스토그램, QQ Plot으로 분포 시각화 가능
------------------------------------------------------------*/

/* 기본 문법(Syntax)
PROC UNIVARIATE DATA = 데이터셋 <옵션>;
    VAR 변수명;
    HISTOGRAM / 옵션;
    QQPLOT / NORMAL;
RUN;
------------------------------------------------------------*/

/* 예시 ① : 기본 통계량 및 정규성 검정 */
proc univariate data = sashelp.cars normal;
    var horsepower;
run;

/*------------------------------------------------------------*/
/* 코드 설명
   ▪ data = sashelp.cars : SAS 내장 데이터셋
   ▪ VAR horsepower : 분석할 수치형 변수 지정
   ▪ NORMAL 옵션 : 정규성 검정 수행 (Shapiro-Wilk, KS 등)
   ▪ 출력: 최소/최대값, 평균, 중앙값, 표준편차, 왜도, 첨도 등
------------------------------------------------------------*/

/* 예시 ② : 히스토그램과 QQ Plot 포함 */
proc univariate data = sashelp.cars normal plot;
    var mpg_city;
    histogram mpg_city / normal(mu=est sigma=est) midpoints=10 to 40 by 5;
    qqplot mpg_city / normal(mu=est sigma=est);
run;

/*------------------------------------------------------------*/
/* 주요 옵션 설명
   ▪ NORMAL : 정규성 검정 결과 포함
   ▪ PLOT : 기본 그래프 (히스토그램, QQ Plot 등) 출력
   ▪ HISTOGRAM / NORMAL : 정규분포 곡선을 함께 표시
   ▪ QQPLOT / NORMAL : 정규분포에 대한 적합도 시각화
   ▪ MU=EST, SIGMA=EST : 평균과 표준편차를 데이터에서 추정
------------------------------------------------------------*/

/* 예시 ③ : 특정 변수 여러 개 분석 */
proc univariate data = sashelp.cars;
    var mpg_city mpg_highway weight;
run;

/*------------------------------------------------------------*/
/* 주요 포인트
   ▪ PROC MEANS보다 상세한 통계 정보 제공
   ▪ 정규성 검정 결과(W, p-value)로 데이터의 분포 특성 확인
   ▪ 그래프 옵션으로 분포를 직관적으로 시각화 가능
------------------------------------------------------------*/
