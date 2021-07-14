select s.stock_name, t2.total_received-t1.total_paid as capital_gain_loss from Stocks s
join
(select stock_name,
sum(price) as total_paid
from Stocks
where operation="Buy"
group by stock_name
)
t1
on s.stock_name=t1.stock_name
join
(select stock_name,
sum(price) as total_received
from Stocks
where operation="Sell"
 group by stock_name
)
t2
on t1.stock_name=t2.stock_name
group by stock_name