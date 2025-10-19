# SELECT의 중첩
서브쿼리가 FROM절에 오면 SELECT \문끼리 중첩된다. 이를 인라인뷰라고 한다. 
SELECT * FROM (SELECT name, popu, area FROM CITY) A;
SELECT * FROM (SELECT * FROM CITY WHERE metro = 'y') B;


# 미성년자 중에 예치금 10만 이상인 사람 찾기
SELECT member, addr FROM (SELECT * FROM tMember WHERE age < 19) A
WHERE A.money > 100000
# 인라인뷰로 미성년자를 먼저 찾고, WHERE절로 10만 이상인 사람 찾기