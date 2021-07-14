select c.name as customer_name, o.customer_id, o.order_id, o.order_date from
(select customer_id, order_id, order_date, RANK() OVER (PARTITION BY customer_id order by order_date DESC) as rnk from Orders) o
join
Customers c
on c.customer_id=o.customer_id
where o.rnk <= 3
order by customer_name, c.customer_id, o.order_date desc

# JOINS

select c.name as customer_name, o3.cid as customer_id, o3.oid as order_id, o3.od as order_date from customers c
join
(select o1.order_id as oid, O1.customer_id as cid, O1.order_date as od, count(*) as rnk
from Orders o1
join Orders o2
on o1.customer_id=o2.customer_id and o1.order_date<=o2.order_date
group by o1.customer_id, o1.order_date) o3
on c.customer_id=o3.cid
where o3.rnk <=3
order by customer_name, c.customer_id, o3.od desc