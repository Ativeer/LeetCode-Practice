# Write your MySQL query statement below

select p.product_name, o.product_id, o.order_id, o.order_date from
(select *, RANK() over (PARTITION BY product_id order by order_date desc) as rnk from Orders) o
join products p on o.product_id=p.product_id
where rnk=1
order by p.product_name, o.order_id