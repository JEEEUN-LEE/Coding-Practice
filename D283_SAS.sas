/* KEEP, DROP*/
DATA XX: 새로운 테이블 XX를 생성한다.
SET YY: 기존 테이블 YY를 불러온다.
KEEP ZZ: 칼럼 ZZ를 테이블에서 유지한다.
DROP PPP: 칼럼 PP를 테이블에서 버린다.

/*IF문*/
DATA TEST;
SET SASHELP.CLASS;
IF AGE = 12; /*12가 아닌 경우는 ^=12로/ 12, 13은 IN (12, 13)*/
RUN;
