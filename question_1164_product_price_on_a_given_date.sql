select DISTINCT p1.product_id,
IFNULL(p2.new_price, 10)
as price
from products p1
LEFT JOIN
(select *
from products
WHERE (product_id, change_date) in
(select product_id, max(change_date) as lasts from Products where change_date <= "2019-08-16" group by product_id) ) p2
on p1.product_id=p2.product_id