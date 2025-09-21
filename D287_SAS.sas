
DATA b1;SET a1;                                        
hei_k = hei /100;                                        
bmi = wei/(hei_k*hei_k);                                 
IF age < 10           THEN    age_g = 1;               
IF 10 <=  age <=30    THEN age_g=2;                    
IF 40 <=  age         THEN age_g=3;                    
IF gender ="F" OR wei <= 23 THEN chk=1;               
ELSE chk=2;                                             
PROC PRINT;                                            
RUN;  

data c1; set a1;
if gender = "M" and hei > 175 then delete; /*관측치 삭제*/

/* 날짜 데이터 핸들링*/
/* SAS에서 날짜를 계산하려면 numeric data value여야한다. 자동으로 날짜형 인식 X */

data test;
today = today();
format today yesterday date9.; /*format으로 날짜 형식 지정하여 출력(yesterday도 날짜 형식 변환 필수)*/ 
yesterday = today - 1;
run;
proc print data = test; run;


/* INTNX()는 date increment를 수행하는 함수로 날짜 간 이동을 실행한다. */
data test3;
birthday = '20APR2023'd;
format birthday date9.;
prepare = intnx('month', birthday, -1)
format prepare date9.;
run;
proc print data = test3; run;
