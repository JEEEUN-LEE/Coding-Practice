/*Where 구문 */
data mysas.where3;
set mysas.example1;
where score >=90 or major = 'Statisticcs';
run;

proc print data = mysas.where3;
run;