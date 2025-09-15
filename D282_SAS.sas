/*자료 분석하기*/
PROC MEANS; VAR hei wei age; /*변수 hei, wei, age의 평균값 등 기술 통계량을 구한다*/
PROC REG; MODEL wei = hei; /*종속변수 wei, 독립변수 hei로 하는 회귀방정식을 구한다 */
bmi = wei / (hei/100) **2; /*bmi 구하기*/

