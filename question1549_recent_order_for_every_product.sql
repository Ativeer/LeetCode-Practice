# Write your MySQL query statement below

select p.product_name, o.product_id, o.order_id, o.order_date from
(select *, RANK() over (PARTITION BY product_id order by order_date desc) as rnk from Orders) o
join products p on o.product_id=p.product_id
where rnk=1
order by p.product_name, o.order_id


# Using Join

select p.product_name, p.product_id, o1.order_id, o1.order_date
from orders o1 join products p on p.product_id=o1.product_id
WHERE
(p.product_id, o1.order_date)
IN
(select product_id, max(order_date) as m from Orders
group by product_id)

order by p.product_name, o1.order_id