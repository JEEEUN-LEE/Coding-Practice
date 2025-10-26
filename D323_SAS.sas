/* 데이터 전처리 및 변수 재코딩 */
data project;
    set a;

    /* 1️⃣ 결측값 제거 및 단위변환 */
    if HE_ht = . then delete;              /* 키 결측 시 삭제 */
    else HE_ht1 = HE_ht / 100;             /* cm → m 단위 변환 */

    if HE_wt = . then delete;              /* 몸무게 결측 시 삭제 */

    /* 2️⃣ BMI 계산 및 범주화 */
    if HE_wt / (HE_ht1 * HE_ht1) < 25 then BMI_Final = 1;   /* 정상 */
    else if 25 <= HE_wt / (HE_ht1 * HE_ht1) then BMI_Final = 2;  /* 과체중 이상 */

    /* 3️⃣ 스트레스 수준 분류 */
    if BP1 in (1, 2) then stress = 1;      /* 낮음 */
    else if BP1 in (3) then stress = 2;    /* 중간 */
    else if BP1 in (4) then stress = 3;    /* 높음 */
    else delete;                           /* 잘못된 값 제거 */

    /* 4️⃣ 교육 수준 분류 */
    if educ in (1, 2, 3, 4, 5) then edu_final = 1;  /* 초/중등 */
    else if educ = 6 then edu_final = 2;            /* 고등 */
    else if educ in (7, 8) then edu_final = 3;      /* 대졸 이상 */
    else delete;

    /* 5️⃣ 소득 수준 범주화 */
    if income <= 2400 then incomepart = 1;           /* 저소득 */
    else if income <= 4800 then incomepart = 2;      /* 중하 */
    else if income <= 7440 then incomepart = 3;      /* 중상 */
    else if income > 7440 then incomepart = 4;       /* 고소득 */
run;
