WITH max_count AS(
    SELECT MAX(CONVERT(DATE, order_date, 105)) AS max_date FROM orders
)

SELECT 
customer_id,
DATEDIFF(DAY,MAX(CONVERT(DATE, order_date, 105)) , (SELECT max_date FROM max_count)) AS recency,
COUNT(order_id) AS frequency,
SUM(final_amount) AS monetary
FROM orders
WHERE order_status = 'Delivered'
GROUP BY customer_id;


-- recency: find the customer maximum date and get the difference
-- frequency count the total number of successful, completed orders
-- monetary: sum up the total life time revenue

-- in the end it should look like customer_id, customer most recent purchase, difference in day, count 
-- of the total orders and sm of total lifetime revenue