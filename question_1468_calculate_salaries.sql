# Write your MySQL query statement below


select s.company_id, s.employee_id, s.employee_name, round(s.Salary*s1.Ratio, 0) as Salary from
Salaries s
join
(select company_id, 
CASE WHEN max(SALARY) < 1000 Then 1
When max(Salary) < 10000 Then 0.76
ELSE 0.51
END
as Ratio
from Salaries
group by company_id) s1

on s.company_id=s1.company_id