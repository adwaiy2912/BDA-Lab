sales_data = LOAD '/Desktop/220968206/week5/sales_data.csv' USING PigStorage(',') 
AS (order_id:int, product:chararray, category:chararray, amount:float);

sorted_sales_data = ORDER sales_data BY amount DESC;

DUMP sorted_sales_data;
STORE LIMITED_DATA INTO '/Desktop/220968206/week5/OUTPUT4' USING PigStorage(',');
