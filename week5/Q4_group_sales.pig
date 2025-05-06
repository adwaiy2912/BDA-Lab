sales_data = LOAD '/Desktop/220968206/week5/sales_data.csv' USING PigStorage(',') 
AS (order_id:int, product:chararray, category:chararray, amount:float);

grouped_by_category = GROUP sales_data BY category;

total_sales_by_category = FOREACH grouped_by_category GENERATE group 
AS category, SUM(sales_data.amount) AS total_sales;

DUMP total_sales_by_category;
STORE LIMITED_DATA INTO '/Desktop/220968206/week5/OUTPUT5' USING PigStorage(',');
