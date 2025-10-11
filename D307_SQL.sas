/*-----------------------------------------------------------
 SQL - 데이터 집계 함수 (Aggregate Functions)
-----------------------------------------------------------*/

/*
 집계 함수란?!
 - 여러 행(Row)의 값을 하나의 결과값으로 요약하는 함수.
 - 주로 GROUP BY와 함께 사용되지만, 단독으로도 전체 집계 가능.
 - NULL 값은 계산에서 제외됨.
 
 주요 집계 함수:
   1) COUNT() : 행의 개수
   2) SUM()   : 합계
   3) AVG()   : 평균
   4) MAX()   : 최댓값
   5) MIN()   : 최솟값
*/


/*-----------------------------------------------------------
 1. COUNT() : 데이터 개수 세기
-----------------------------------------------------------*/

-- name 컬럼의 데이터 개수 반환 (NULL 제외)
SELECT COUNT(name)
FROM Artist;

-- DISTINCT를 사용해 중복을 제거하고 고유 ArtistId 개수 계산
SELECT COUNT(DISTINCT ArtistId) AS unique_artist_cnt
FROM Album;



/*-----------------------------------------------------------
 2. SUM() : 합계 구하기
-----------------------------------------------------------*/

-- fruit_prices 테이블의 retailprice 합계 구하기
SELECT SUM(retailprice)
FROM fruit_prices;

-- AS 키워드로 별칭(alias) 지정
SELECT SUM(retailprice) AS price
FROM fruit_prices;

-- 여러 컬럼의 합계 동시 계산 (retailprice, retailpriceunit)
SELECT 
    SUM(retailprice) AS total_price, 
    SUM(retailpriceunit) AS total_unit
FROM fruit_prices;



/*-----------------------------------------------------------
 3. AVG() : 평균값 구하기
-----------------------------------------------------------*/

-- price 컬럼의 평균값 계산
SELECT AVG(price)
FROM fruit_prices;

-- retailprice의 평균값을 avg_price라는 별칭으로 출력
SELECT AVG(retailprice) AS avg_price
FROM fruit_prices;



/*-----------------------------------------------------------
 💡 참고:
 - COUNT(*) : NULL 포함 전체 행 수
 - COUNT(column) : NULL 제외
 - SUM(), AVG() : NULL 제외하고 계산
 - AS : 결과 컬럼명에 별칭을 지정할 때 사용
-----------------------------------------------------------*/
