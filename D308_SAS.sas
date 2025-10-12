/*SAS- 범주형 변수 처리*/
/*if 문으로 숫자형 데이터를 범주형 데이터로 변환하기*/
data work.bacteria_new;
set sasuser.bacteria;
	if temp < 10 then
		temp_category = 0;
	else if temp >= 10 and temp < 20 then
		temp_category = 1;
	else if temp >= 20 and temp < 30 then
		temp_category = 2;
	else if temp >= 30 and temp < 40 then
		temp_category = 3;
	else if temp >= 40 and temp < 50 then
		temp_category = 4;
	else
		temp_category = 5;
	drop temp;
run;
