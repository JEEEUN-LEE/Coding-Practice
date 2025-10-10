/*-----------------------------------------------------------
 SQL - WHERE절 및 집합 연산자
-----------------------------------------------------------*/

/* 집합 연산자 종류
   1) UNION       : 두 집합을 합침 (중복 제거)
   2) UNION ALL   : 두 집합을 합침 (중복 제거 안 함)
   3) INTERSECT   : 두 집합의 교집합
   4) EXCEPT      : 첫 번째 집합에서 두 번째 집합을 제외
*/


-- UNION : 중복 제거
SELECT trackid
FROM Track
UNION
SELECT trackid
FROM InvoiceLine;


-- UNION ALL : 중복 제거하지 않음
SELECT trackid
FROM Track
UNION ALL
SELECT trackid
FROM InvoiceLine;


-- INTERSECT : 두 집합의 교집합 (공통된 데이터만 반환)
SELECT trackid
FROM Track
INTERSECT
SELECT trackid
FROM InvoiceLine;


-- EXCEPT : 차집합 (첫 번째 집합에서 두 번째 집합을 제외)
SELECT trackid
FROM Track
EXCEPT
SELECT trackid
FROM InvoiceLine;



/*-----------------------------------------------------------
 SQL 쿼리 실행 및 작성 순서
-----------------------------------------------------------*/

/*
 [작성 순서] : SELECT > FROM > WHERE > GROUP BY > HAVING > ORDER BY
 [실행 순서] : FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

 - SELECT : 조회할 컬럼 지정
 - FROM : 데이터를 가져올 테이블 지정
 - WHERE : 조건에 맞는 행 필터링
 - GROUP BY : 특정 컬럼 기준으로 그룹화
 - HAVING : 그룹화된 결과에 조건 적용
 - ORDER BY : 결과 정렬
*/


SELECT
    Form,
    COUNT(fruit) AS fruit_cnt
FROM
    Fruit_price
WHERE
    Retailpriceunit >= 1
GROUP BY
    Form;



/*-----------------------------------------------------------
 ML - K-Means++
-----------------------------------------------------------*/

/*
 K-Means의 문제점:
  - 초기 중심점(Centroid)을 무작위로 선택하면 결과가 불안정할 수 있음
  - 이를 '랜덤 초기화 함정(Random Initialization Trap)'이라 부름

 K-Means++의 목적:
  - 중심점을 더 효율적으로 선택하여 알고리즘의 성능 개선
*/


/*
 [K-Means++ 알고리즘 절차]

 1. 데이터 중 1개를 무작위로 선택하여 첫 번째 중심점으로 지정
 2. 선택된 중심점을 제외한 나머지 데이터와의 거리를 계산
 3. 중심점에서 가장 먼 지점을 다음 중심점으로 선택
 4. 중심점이 K개가 될 때까지 2~3단계 반복
 5. 이후 일반적인 K-Means 알고리즘 수행 (군집화 반복)
*/
