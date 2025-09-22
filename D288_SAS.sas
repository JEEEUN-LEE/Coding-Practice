/*SCAN 문자열 분할 & 단어 추출*/
/*SCAN 구분자 기준으로 문자열 분할하여 특정 순서 단어를 추출 SCAN(string, n, delimiter)*/
data separater_test1;
set WORK.IMPORT1;
firstname = scan(customer_name, 1, ' ' ); /*공백 기준으로 첫번째 단어 추출*/
keep customer_name firstname;
run;

data separater_test1;
set WORK.IMPORT1;
firstname = scan(customer_name, 1, ' ');
lastword = scan(customer_name, -1, ' '); /*마지막 단어 추출*/
keep customer_name firstname lastword;
run;

/*INDEX 문자열 위치 찾기*/
data test;
set sashelp.zipcode;
run;

data test2;
set test;
idx = index(city, 'Addis');
if idx > 0; 
run; /* 특정 단어가 처음 등장하는 위치를 출력함. idx >0이면 특정 문자 포함된 것만 추출*/

data test2;
set test;
idx = index(upcase(countynm), 'D');
if idx > 0;
run;
