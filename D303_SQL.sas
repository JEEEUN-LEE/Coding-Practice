/*SQL- 혼동하기 쉬운 부분*/

/*Where & Having 절*/
/*Where 절은 From절에서 테이블을 필터링 한다, Having절은 Group by로 만들어진 테이블을 필터링 한다*/
select form, avg(yield) as avg_yield
from Fruit_Prices
where Yied > 0.5
group by form  /*form 별로 그룹화하며 avg_yield 생성*/
having retailprice > 1.2

/*Where & On*/
/*Where는 from 절 테이블을 필터링하고, On은 Join절인 테이블 간 결합 조건의 기준을 세운다*/
select a.invoiceid, a.customerId, a.total, b.FirstName
from Invoice as a
join customer as b
on a.customer_id = b.customer_id
where a.total > 5
