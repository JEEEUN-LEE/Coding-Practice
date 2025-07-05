# SUBSTR
## SUBSTR(문자열, N1, N2) : 문자열 또는 문자형 변수의 N1번째 문자부터 총 N2자리 문자열 추출
DATA TEMP;
BASE_DATE = '20191231';
BASE_MONTH = SUBSTR(BASE_DATE, 1,4); /*BASE_DATE의 첫번째 문자부터 총 4자리 문자열만 추출*/
RUN;