/*PROC SQL- Order by*/
/* 기본 틀 
select * from table_name
order by column_name (asc, desc); 내림차순, 오름차순 정렬할 때 사용*/

filename refile '/home/u/occupations.xlsx';
proc import datafile = refile 
	dbms = xlsx
	out = work.occupations;
	getnames = yes;
run;

proc contents data= work.occupation; run;
proc sql;
	select cats(name, '(', substr(occupation, 1, 1), ')' ) from work.occpations
	order by name;
/* Adam(S), Carloll(P) .. */

proc sql;
	select cats('there are a total of  ', count(*), ' ', lower(occupation), 's.')
	from occupations
	group by occupation
	oder by occupation;
quit; /*occpuation별로 그룹화해서, 집계, cat는 문자열 그대로 이어붙이고 cats는 문자열 끝에 공백 제거 후 이어붙이기*/

