SELECT * FROM (
        SELECT name, popu * 10000 AS ingu FROM tCity
) A
WHERE A.ingu > 1000000;

# 인구밀도로 등급 나누기
SELECT name, (popu*1000 / area) AS dens
    , CASE 
        WHEN(popu * 10000 / area) > 1000 THEN '고밀도'
        WHEN(popu * 10000 / area) > 100 THEN '중밀도'
        ELSE '저밀도
    END densgrade
FROM tCity;

# SELECT문 중첩
SELECT name, dens, densgrad,
CASE 
    WHEN densgrade = '고밀도' THEN '8차로'
    WHEN densgrade = '중밀도' THEN '4차로'
    ELSE '2차로'
END roadplan
FROM
(
    SELECT name, dens
        , CASE 
                WHEN dens > 1000 THEN '고밀도'
                WHEN dens > 100 THEN '중밀도'
                ELSE '저밀도'
        end densegrade
    FROM 
    (
        SELECT name, (popu * 10000 / area) AS dens FROM tCity
    ) CD
) CR;
