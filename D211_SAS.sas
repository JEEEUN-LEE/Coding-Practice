#CATS 함수
## CATS(문자열1, 문자열2, 문자열3..):문자열 또는 문자형 변수 걸합 함수
DATA TEMP;
BASE_MONTH ='201912'
BASE_DATE1 = CATS(BASE_MONTH, '01');
BASE_DATE2 = CATS(BASE_MONTH, ' 01 ');
RUN;

CATS 함수는 곤백을 다 제거하고 결합함