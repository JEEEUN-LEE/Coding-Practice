# SAS 주요 데이터 클리닝
## Keep: 필요한 변수만 데이터셋 남길 때 keep 문장을 사용
## PROC CONTENTS: 특정 데이터셋의 관측치의 수, 변수 수, 변수 유형, 변수 길이 파악
## RENAME: 변수명 변경
data mysas.bweight_rename;
	set mysas.bweight;
	rename smoke = smoking;
run;
## Sum: 변수 연산
black_boy = sum(black, boy);

