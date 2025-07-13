# SORT 프로시저
PROC SORT DATA = mysas.htwt OUT = new_htwt;
run;

PROC SORT DATA = mysas.htwt OUT = new_htwt NODUPKEY;
	BY dept DESCENDING height;
RUN;