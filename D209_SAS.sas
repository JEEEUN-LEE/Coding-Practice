# PROC SORT
데이터 정렬 및 중복 제거를 위해 사용 (디폴트 오름차순)
PROC SORT DATA = SASHELP.HEART; 
BY DESCENDING STATUS; RUN;

보통 중복 제거하기 위해 더 자주 이용(정렬하고, 중복제거)
PROC SORT DATA = SASHELP.HEART
 OUT = SASHELP.HEART_1
 DUPOUT = SASHELP.HEART_2
 NODUPKEY;
 BY STATUS;
RUN;
* 정렬 먼저 한 후, 중복 제거
* NODUPKEY를 사용해서 BY 변수의 값이 같은 행 중 첫번 째만 남김.
