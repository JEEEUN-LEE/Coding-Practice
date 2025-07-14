# sas로 하는 기초 데이터 전처리 핸들링
관련 링크: https://wikidocs.net/31021

## 1. SAS 기초
data xxx: 테이블을 생성하는 명령어
set yyy: 테이블을 불러오는 명령어
run: 코드 끝을 알려주는 명령어

- 테이블 앞에 라이브러리명을 지정하지 않을 경우 WORK 라이브러리로 인식하거나 저장한다.
- 실무에선 데이터를 가져와서, 다른 라이브러리에 복사한 후 그 파일을 가공해서 사용함.

LIBNAME SASSET "C:\SAS\BASE"; 라이브러리명 SASSET 생성

LIBNAME SASTEST "C:\SAS";

DATA SASTEST.TEST;
SET SASHELP.CLASS;
RUN;

## 다음 차수: PROC 사용