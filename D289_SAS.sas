/*SUBSTR 문자열 추출 & 치환*/
/*SUBSTR(변수, startpos, length) startpos부터 length만큼 추출*/
data test1;
set sashelp.zipcode;
first3 = substr(city, 1, 3);
run;

data test1;
set sashelp.zipcode;
idxxpace = index(city, ' ' ); /* 첫번째 공백이 나오는 위치를 찾아 저장*/
first3 = substr(city, 1, 3);
run;

data test1;
set sashelp.zipcode;
idxxpace = index(city, ' ');
first3 = substr(city, 1, 3);
substr(city, 1, idxxpace) = 'Wakanda'; /*첫번째 공백을 'Wakanda'로 치환, 공백 없으면 idxxpace = 0으로 치환되지 않음*/
run;