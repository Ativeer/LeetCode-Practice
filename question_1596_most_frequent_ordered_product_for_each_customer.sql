select c.customer_id, c.product_id, p.product_name from

(select customer_id, product_id, RANK() OVER (partition by customer_id order by cnt desc) as rnk from
(select customer_id, product_id, count(*) as cnt from Orders 
group by customer_id, product_id
order by customer_id, cnt desc) a) c
join Products p
on c.product_id=p.product_id
where c.rnk=1