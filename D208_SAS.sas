[프로시저]
https://icefree.tistory.com/entry/SAS-%EC%9E%90%EC%A3%BC-%EC%93%B0%EB%8A%94-%EA%B8%B0%EB%8A%A5-%EC%A0%95%EB%A6%AC

# PROC CONTENTS 
테이블 길이, 변수 목록, 변수의 자료형 등의 정보 출력
PROC CONTENTS DATA = SASHELP.HEART; RUN;
# PROC MEANS
특정 기술 통계량 옵션 지정, 지정안하면 기본 5개 기술 통게량 제공
PROC MEANS DATA = SASHELP.HEART; 
 CLASS GENDER;
 VAR TOTAL_SCORE;
RUN;
# PROC FREQ
데이터 테이블의 빈도 조회
PROC FREQ DATA = SASHELP.HEART;
 TABLES Status Smoking_Status;
RUN;
**빈도 외 수치 없애는 옵션
PROC FREQ DATA = SASHELP.HEART;
 TABLES Status / NOCOL NOROW NOCUM NOPERCENT MISSING;
RUN;
