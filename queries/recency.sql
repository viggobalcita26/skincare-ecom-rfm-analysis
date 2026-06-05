WITH max_count AS(
    SELECT MAX(CONVERT(DATE, order_date, 105)) AS max_date FROM orders
)

SELECT 
customer_id,
DATEDIFF(DAY,MAX(CONVERT(DATE, order_date, 105)) , (SELECT max_date FROM max_count)) AS days_since_last_order
FROM orders
WHERE order_status = 'Delivered'
GROUP BY customer_id;

