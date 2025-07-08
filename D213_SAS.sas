# INTNX / INTCK 날짜 연산 함수
## INTNX(interval, 기준날짜, interval 증감) : 기준날짜로부터 특정 기간 이전/ 후 날짜 산출함
## 마지막 인자로 'S', 'B', 'E' 알파벳을 추가하여 특정 일 반환 지정 가능
DATA TMP;
BASE_DATE = INPUT('20191231', YYYYMMN8.);
/*1일 전*/
BASE_DATE_1D = INTNX('DAY', BASE_DATE, -1);
/*1개월 전 첫 일자*/
BASE_DATE_1M_B = INTNX('MONTH', BASE_DATE, -1, 'B');
/*1년 전 동일한 일자*/
BASE_DATE_1Y = INTNX('YEAR', BASE_DATE, -1, 'S');
RUN;

# INTCK 함수
##  INTCK(interval, 날짜1, 날짜2): 날짜 1과 날짜2 사시의 기간 산출
DATA TMP;
start = INPUT('20181130', yymmdd8.);
end = INPUT('20191231', yymmdd8.);
/*일단위 기간*/
interval_day = intck('day', start, end) 
/*월 단위*/
interval_month = intck('month', satrt, end)
/*연 단위*/
interval_year = intck('year', start, end)
run;
