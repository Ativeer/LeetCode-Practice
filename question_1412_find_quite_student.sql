# Write your MySQL query statement below



select DISTINCT(s4.student_id), s4.student_name from student s4
join exam e3
on s4.student_id=e3.student_id
where
(s4.student_id) NOT IN
(select DISTINCT(s1.student_id) from student s1
join
exam e1
on s1.student_id=e1.student_id
join
(select e.exam_id as ex, max(e.score) as ex_max, min(e.score) as ex_min from student s join exam e on s.student_id=e.student_id
group by e.exam_id) s2
on e1.exam_id=s2.ex
where e1.score=s2.ex_max or e1.score=s2.ex_min)
order by s4.student_id