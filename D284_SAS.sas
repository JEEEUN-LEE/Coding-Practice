# SAS

# 3.4.1 DATA문의 형태
## 데이터셋 이름 여러 개 지정하는 경우
DATA a1 a2 a3;
SET a1;
IF x=1 THEN OUTPUT b1;
ELSE x=2 THEN OUTPUT b2;
ELSE x=3 THEN OUTPUT b3;