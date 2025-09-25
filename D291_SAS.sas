/*문자형 변수*/
/*대문자 변환: UPCASE()*/
data upcase_test;
set _test1_;
upcase = upcase(name);
run;
/*소문자 변환: LOWCASE()*/

/*TRIM() : 뒤쪽 공백 제거 함수(문자열 끝 쪽 공백 제거) */
/*CAT() : 문자열 그대로 공백 제거 없이 연결 */
data cat;
full_text = cat(text1, text2, text3);
put full_text;
run;
/*CATS() : 앞뒤 공백 제거하면서 연결*/
/*CATX() : 구분자 지정해서, 앞뒤 공백 제거하여, 문자열 연결*/
