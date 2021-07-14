# Write your MySQL query statement below
SELECT person1, person2, sum(call_count) as call_count, sum(total_duration) as total_duration  FROM
(select from_id as person1, to_id as person2, count(*) as call_count, sum(duration) as total_duration
from Calls
where from_id<to_id
group by from_id, to_id


UNION

select to_id as person1, from_id as person2, count(*) as call_count, sum(duration) as total_duration
from Calls
where from_id>to_id
group by from_id, to_id)

t1
group by person1, person2