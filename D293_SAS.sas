# 돌연한 출발

/*데이터 가져오기*/
proc import out = work.customer;
datafile = 'C:/customers.xlsx'
dbms = xlsx;
replace;
getnames = yes;
run;

proc print data = work.customer; run;

/*데이터 병합*/
proc sql;
create table merge_data as;
select A.*, B.*, C.*
from work.sales as A
left join work.customer as B
	on A.cutomer_id = B.id
left join work.products as C
	on A.product_id = C.id;
quit;

proc print data = merge_data(obs = 20); run;

/*고객별 매출 집계*/
proc sql;
create table work.precus as 
select customer_name, sum(profit) as profit
from work.merge_data
group by customer_name
order by profit desc;
quit;
run;

/*SAS 기본 실무 문법 데이터 불러오기, 요약 통계, 정렬*/
/*1. Import 데이터 불러오기*/
proc import out = baseball datafile = 'C:/baseball.xlsx' dbms = xlsx replace;
getnames = yes;
run;
/*2. 데이터 분포 확인*/
proc means data = baseball; run;
/*3. 데이터 정렬*/
proc sort data = baseball; by descending nHome; run;

proc sort data = baseball(obs = 5); by descending salary; run;

/*회귀분석- out 횟수가 연봉에 미치는 영향*/
proc reg data = baseball;
model salary = nOuts; /*종속변수 salary, 독립변수 nOuts*/ 
run; 

/*다음 시간 회귀분석 결과 해석 마저..*/
