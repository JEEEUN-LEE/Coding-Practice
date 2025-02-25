# 프로그래머스: 대장균의 크기에 따라 분류하기 2
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/301649

# 서브 쿼리: 대장균 개체의 크기 기준으로 내림차순 정렬하고, 백분율 구하기
# 메인 쿼리: 백분율 값에 따라 4개로 범주화
# ID 기준 오름차순 정렬
SELECT A.ID,
       CASE
           WHEN A.PER <= 0.25 THEN 'CRITICAL'
           WHEN A.PER <= 0.50 THEN 'HIGH'
           WHEN A.PER <= 0.75 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS COLONY_NAME
FROM (
    SELECT ID, 
           PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER
    FROM ECOLI_DATA
) AS A
ORDER BY A.ID;