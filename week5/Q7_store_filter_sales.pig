sales_data = LOAD '/Desktop/220968206/week5/sales_data.csv' USING PigStorage(',') 
AS (order_id:int, product:chararray, category:chararray, amount:float);

high_value_transactions = FILTER sales_data BY amount > 5000;

DUMP high_value_transactions;

STORE high_value_transactions INTO '/user/220968424/lab5/output/high_value_transactions' USING PigStorage(',');
STORE LIMITED_DATA INTO '/Desktop/220968206/week5/OUTPUT8' USING PigStorage(',');
