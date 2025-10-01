/*------------------------------------------------------*/
/* SAS Macro: %LET 선언                                  */
/* %LET 매크로변수 = 값;                                 */
/* %LET으로 선언하면 글로벌 매크로 변수로 사용됨          */
/*------------------------------------------------------*/

/* 예시 1: %LET을 활용한 전역 변수 */
%let libname = sashelp;
%let data = air;

proc print data=&libname..&data;  /* libname과 data 결합: sashelp.air */
run;



/* 예시 2: 매크로 내부 변수 */
%macro test1;
    %let model = SUV; 
    %put Local variable model = &model;   /* 로그창에 출력 */
%mend;

%test1;

/* 매크로 밖에서 호출하면 값이 없음 */
%put &model;



/* 예시 3: 조건문에서 %LET 사용 */
%macro test(var);
    %if &var = %then %do;
        %put WARNING: var 값이 비어 있습니다.;
    %end;
    %else %do;
        %put NOTE: var 값은 &var 입니다.;
    %end;
%mend;

%test();        /* var 값이 비어 있습니다 */
%test(100);     /* var 값은 100입니다. */



/*------------------------------------------------------*/
/* SAS Macro: %DO 반복문                                */
/* %DO 변수 = 시작값 %TO 종료값 %BY 증분;                */
/*------------------------------------------------------*/

/* 예시 1: 1부터 5까지 반복 */
%macro loop_ex1;
    %do i = 1 %to 5;
        %put No: &i;
    %end;
%mend;

%loop_ex1;


/* 예시 2: 50부터 30까지 -2씩 감소 */
%macro loop_ex2;
    %do i = 50 %to 30 %by -2;
        %put No: &i;
    %end;
%mend;

%loop_ex2;