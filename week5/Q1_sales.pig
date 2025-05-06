sales_data = LOAD '/user/220968424/lab5/sales_data.csv' USING PigStorage(',')
AS (order_id:int, product:chararray, category:chararray, amount:float);

LIMITED_DATA = LIMIT sales_data 10;

DUMP LIMITED_DATA;

