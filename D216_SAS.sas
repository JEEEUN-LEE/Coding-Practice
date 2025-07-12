proc sql;
	create table T2_A1 as select distinct
	 sg, age, count(distinct mid) as n_mid, round(avg(VST_DDCNT), 0.01) as av_vst, round(std(vst_ddcnt), 0.01) as std_vst, round(avg(RVD_RPE_TAMT_AMT), 0.01) as av_amt, round(std(RVD_RPE_TAMT_AMT), 0.01) as std_amt
	from aa.t20_sg
	group by sg.age;
quit;