# Write your MySQL query statement below



select user_id, max(diff) as biggest_window from
(select *,
(case when
rw = 1 then DATEDIFF("2021-01-01", visit_date)
else DATEDIFF(lag(visit_date, 1) over (), visit_date)
end)
as diff from
(select *, row_number() over(partition by user_id order by visit_date DESC) as rw from UserVisits)
v1) v2

group by user_id