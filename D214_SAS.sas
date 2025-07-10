# PROC FREQ
PROC FREQ DATA = SASHELP.HEART;
	TABLES Smoking_Status;
RUN;

PROC FREQ DATA = SASHELP.HEART;
	TABLES Smoking_Status*Status;
RUN;
**2개 이상 변수를 연결하면 행*열로 교차된 테이블을 추출한다.