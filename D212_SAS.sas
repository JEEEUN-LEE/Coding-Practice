# INPUT / PUT -TYPE 변환 함수
## INPUT(변수1, 숫자형식): 문자형-> 숫자형으로 변환 
## PUT(변수1, 문자형식): 숫자형-> 문자형으로 변환

/*문자를 숫자형으로*/
DATA TMP;
BASE_MONTH_NUM = INPUT('20191231', YYYYMMN8.); 
BASE_MONTH_NUM = INPUT('20191231',  8.); 

/*숫자를 문자형으로*/
BASE_MONTH_CHRO = PUT(20191231, $8.);
BASE_MONTH_CHR1 = PUT(20191231, YYYYMMN8.);
RUN;
