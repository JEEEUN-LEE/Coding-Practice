/* SQL - Concat: 둘 이상의 문자열 값을 조인 */
concat(string_value1[, string_valueN])
select concat('Hello', 'World', '!');

select col1
concat(null, col1, col2) as col
from table;

select first_name, concat(null, first_name, last_name) as col from table2;

select concat_ws(',', first_name, last_name) as col2 
from table2;

# IFNULL : 대체값 채우기
SELECT *, IFNULL(middle_name, '대체값') AS COL2 FROM TABLE2

# TRIM: 문자열 공백 제거
# SUBSTR : 지정한 범위의 문자열 반환 