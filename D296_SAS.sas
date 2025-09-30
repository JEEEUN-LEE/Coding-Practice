/*------------------------------------------------------*/
/* SAS Macro 예제                                       */
/* 매크로 정의: %MACRO ~ %MEND                          */
/* 매크로 호출: %매크로명(인자1, 인자2, ...)            */
/*------------------------------------------------------*/

/* 매크로 1: 특정 차종만 출력 */
%MACRO print_cars(dataset, car_type);  

    proc print data=&dataset;
        var make model;              /* 제조사, 모델명만 출력 */
        where type = "&car_type";    /* 매크로 변수는 & 사용 */
        title "차량 유형: &car_type";
    run;

%MEND print_cars;

/* 매크로 호출 예제 */
%print_cars(SASHELP.CARS, SUV);

/* 매크로 2: 특정 차종을 필터링해 새 데이터셋 생성 후 출력 */
%MACRO save_filtered_cars(dataset, car_type, output_name);

    data &output_name;
        set &dataset;
        where type = "&car_type"; 
        keep make model type;       /* 필요한 변수만 저장 */
    run;

    proc print data=&output_name;
        title "저장된 데이터: &car_type";
    run;

%MEND save_filtered_cars;


/* 매크로 호출 예제 */
%save_filtered_cars(SASHELP.CARS, SUV, WORK.SUV_CARS);


           DATA &output_name;

                     SET &dataset;

                     WHERE Type = ‘&car_type’;

                     Keep make model type;

           Run;

           Proc print data = &output_name;

                     Title ‘저장된 데이터: &car_type’;

           Run;

&MEND

 
%save_filtered_cars(SASHELP.CARS, SUB, WORK.SUV_CARS); /* WORK.SUV_CARS 새로 저장*/