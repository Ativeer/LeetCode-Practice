# Write your MySQL query statement below
# select q1.person_name from Queue q1 join Queue q2 on q1.turn>=q2.turn
# group by q1.turn
# HAVING sum(q2.weight) <=1000
# order by q1.turn desc
# LIMIT 1

select person_name from
(select person_name, sum(weight) over (order by turn) as w from Queue) a
where w<=1000
order by w DESC
limit 1