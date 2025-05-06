sales_data = LOAD '/Desktop/220968206/week5/sales_data.csv' USING PigStorage(',') 
AS (order_id:int, product:chararray, category:chararray, amount:float);

customers_data = LOAD '/Desktop/220968206/week5/customers_data.csv' USING PigStorage(',') 
AS (order_id:int, customer_name:chararray, city:chararray);

joined_data = JOIN sales_data BY order_id, customers_data BY order_id;

DUMP joined_data;
STORE LIMITED_DATA INTO '/Desktop/220968206/week5/OUTPUT6' USING PigStorage(',');
