/*숫자형식_Numerical Format*/
 /*COMMA6.2 (6은 소수점 포함한 전체 자리수 의미, 2는 소수점 아래 2자리 표시)*/
 /*DOLLAR8.2 (통화와 관련된 데이터 표시할 때, 숫자/기호 등 포함된 8자리, 소수점 2자리 표시*/

/*COMPBL(문자열 또는 문자변수): 문자열 제거*/
/*문자열 앞뒤 공백 제거, 공란 여러개일 때 하나로 변환하는 정제 가능*/
data test1; 
text = 'I     don't know   well.';
text2 = compbl(text);
put text2;
run; /*COMPRESS는 모든 공백 제거라면, COMPBL 연속된 공란에서 하나만 남기고 제거*/

/*COMPRESS: 모든 공백 제거
data city2;
set city;
compress_name = '*' || compress(name) || '*'; /*공백 제거한 상태로 '*' 앞뒤로 붙이기*/

data city2;
set city;
compress_name = compress(name, '*'); /* name 변수에서 '*' 문자 제거하기*/
run; 