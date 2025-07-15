# PROC 사용법
## PROC SORT : 테이블 데이터를 순서대로 정렬한다.
PROC SORT DATA = SASHELP.CLASS OUT = TEST;
BY AGE; /*디폴트: ASCENDING*/
RUN;

PROC SORT DATA = TEST;
BY DECSENDING AGE;
RUN;

## PROC PRINT : 테이블 보여주기
PROC PRINT DATA = TEST;
VAR AGE NAME;
ID AGE;
BY AGE;
RUN;

** BY를 PROC PRINT 하기 위해선 SORTING 먼저 해야함

## PROC CONTENTS : 테이블 속성 보기 
** 테이블명, 라이브러리명, 관측치, 변수, 파일명, 인덱스, 정렬, 파일크기 등을 확인한다.