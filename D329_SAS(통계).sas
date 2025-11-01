/*--------------------------------------------------------------
    PROC SQL - CASE WHEN 문법 정리 및 실습 예제
--------------------------------------------------------------*/

/*
CASE WHEN 구문이란?
조건에 따라 서로 다른 값을 반환하는 제어문으로,
SQL 및 SAS의 PROC SQL에서 자주 사용된다.
*/

/* 기본 구조 예시
CASE 
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result 
END
*/

/*--------------------------------------------------------------
    실습: 삼각형 종류 판별
--------------------------------------------------------------*/

/* 1. 엑셀 데이터 불러오기 */
FILENAME REFILE 'C:\path\to\your\triangles.xlsx';

PROC IMPORT DATAFILE=REFILE
    DBMS=XLSX
    OUT=WORK.triangles
    GETNAMES=YES;
RUN;

/*--------------------------------------------------------------
    2. PROC SQL + CASE WHEN
    - 삼각형의 변 길이 (a, b, c)에 따라 종류 분류
--------------------------------------------------------------*/

PROC SQL;
    SELECT
        a,
        b,
        c,
        CASE 
            WHEN a + b <= c OR a + c <= b OR b + c <= a THEN 'Not a Triangle'  /* 삼각형이 아님 */
            WHEN a = b AND b = c THEN 'Equilateral'                            /* 정삼각형 */
            WHEN a = b OR b = c OR a = c THEN 'Isosceles'                      /* 이등변삼각형 */
            ELSE 'Scalene'                                                     /* 부등변삼각형 */
        END AS Triangle_Type
    FROM WORK.triangles;
QUIT;
