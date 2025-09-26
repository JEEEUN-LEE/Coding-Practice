/*PROC PRINT로 상세한 보고서 만들기*/

/*데이터셋 가져오기*/
PROC IMPORT 
	DATAFILE = XLSX
	REPLACE
	OUT = WORK.SALE;
	GETNAMES = YES;
RUN;

PROC PRINT DATA = WORK.SALE; RUN;
PROC PRINT DATA = WORK.SALE(obs = 20); RUN; /*행 번호 없이는 NOOBS 옵션*/

PROC PRINT DATA = WORK.SALE(obs = 15) noobs;
var sales shipping_cost profit;
where shipping_cost > 10;
format profit dollar9.2; /*달러 형식으로 값을 출력*/
title '비싼 배송비를 지불한 주문 사례';
sum profit;
RUN;

/*그룹화*/
proc print data = sale(obs = 20); run;
proc sort data = sale;
by province;
run;

proc print data = work.sale noobs;
var sales shipping_cost profit;
where shipping_cost > 10;
format profit dollar9.2;
title '~~'
sum profit;
by province;
run;

