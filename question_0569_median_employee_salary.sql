
select e1.id, e1.company, e1.salary from
(SELECT *, ROW_NUMBER() OVER (PARTITION BY COMPANY ORDER BY SALARY ASC, ID ASC) as rn_asc,
ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY SALARY DESC, ID DESC) as rn_desc FROM Employee) e1
where rn_asc between rn_desc-1 and rn_desc+1

# USING COUNT LOGIC

select e1.ID, e1.Company, e1.Salary from
(select company, count(*) as cnt from employee group by company) e2
join
(select *, row_number() over (partition by company order by Salary, ID) rwno
from employee) e1
on e2.company=e1.company 
where e1.rwno between e2.cnt/2 and (e2.cnt/2)+1