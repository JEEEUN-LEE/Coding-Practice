data work.sortedshoes;
set sashelp.shoes;
run;

proc print; run;
proc sort data = shoredshoes;
by descending product sales;
run;

proc print data = sortedshoes(firstobs = 148 obs = 148);
run;
proc print data = sortedshoes(firstobs = 130 obs = 130);
run;