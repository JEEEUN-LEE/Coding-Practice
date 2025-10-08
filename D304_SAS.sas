/*SQL- CASE WHEN&*/
CASE 
	WHEN condition1 THEN result1
	WHEN condition2 THEN result2
	...
	ELSE default_result 
END

/*예시*/
filename refile '/home/u45/triangles.xlsx';

proc import datafile = refile
	dbms = xlsx
	out = work.triangles;
	getnames = yes;
run;

proc sql;
select 
case when a = b and b = c then 'Equilateral'
	when a = b or b = c or a = c then 'Isosceles'
	when a + b <= c or a + c <= b or b+c <= a then 'not a trianles'
	else 'Scalene'
end as New_Column
from work.triangles;

