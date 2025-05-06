sales_data = LOAD '/Desktop/220968206/week5/sales_data.csv' USING PigStorage(',') 
AS (order_id:int, product:chararray, category:chararray, amount:float);

DUMP sales_data;

high_value_sales = FILTER sales_data BY amount > 5000;

DUMP high_value_sales;
STORE LIMITED_DATA INTO '/Desktop/220968206/week5/OUTPUT3' USING PigStorage(',');
