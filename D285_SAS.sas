# 3.5 SET문

# SAS 프로그래밍을 잘짜다는 말은, 얼마나 SAS 데이터셋을 잘 만들 수 있느냐이다.
DATA all; SET a1 a2; /*a1, a2를 아래위로 합치기*/
DATA kkk; SET AB; IF reg = 1; /*AB 데이터셋 중에서 REG가 1인 경우만 kkk에 저장*/
DATA AB; MERGE a1 a2 ; BY reg; /*데이터셋 a1, a2를 reg 기준으로 옆으로 합치기

# 만들어진 데이터셋에서 일부 특성에 맞는 자료만 추출하여 분석하는 경우

DATA a1; SET INFO;
IF gender = ‘F’;
Bmi = wei / (hei/100) **2;
PROC MEANS DATA=a1;
RUN;