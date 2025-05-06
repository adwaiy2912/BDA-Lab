sales_data = LOAD '/Desktop/220968206/week5/sales_data.csv' USING PigStorage(',') 
AS (order_id:int, product:chararray, category:chararray, amount:float);

sorted_sales = ORDER sales_data BY amount DESC;

top_3_expensive_products = LIMIT sorted_sales 3;

DUMP top_3_expensive_products;
STORE LIMITED_DATA INTO '/Desktop/220968206/week5/OUTPUT7' USING PigStorage(',');
