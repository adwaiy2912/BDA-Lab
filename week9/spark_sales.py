from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

spark = SparkSession.builder.appName("Sales Data Processing").getOrCreate()

hdfs_input_path = "hdfs://localhost:9000/user/220968424/lab9/sales_data.csv"
hdfs_output_path = "hdfs://localhost:9000/user/220968424/lab9/output3/"

# a) Load a CSV file from HDFS into a Spark DataFrame.
df = spark.read.csv(hdfs_input_path, header=True, inferSchema=True)
df.show()
df.write.csv(f"{hdfs_output_path}/a_loaded_data/", header=True)

# b) Compute total revenue per product (Revenue = Price * Quantity).
df = df.withColumn("Revenue", col("Price") * col("Quantity"))
df.select("Product", "Revenue").show()
df.select("Product", "Revenue").write.csv(f"{hdfs_output_path}/b_total_revenue/", header=True)

# c) Find the highest-selling product (by revenue).
highest_selling_product = df.orderBy(col("Revenue").desc()).limit(1)
highest_selling_product.show()
highest_selling_product.write.csv(f"{hdfs_output_path}/c_highest_selling/", header=True)

# d) Filter transactions where total sales are above $500.
filtered_df = df.filter(col("Revenue") > 500)
filtered_df.show()
filtered_df.write.csv(f"{hdfs_output_path}/d_filtered_sales/", header=True)

# e) Group by category and compute total revenue per category.
category_revenue_df = df.groupBy("Category").agg(sum("Revenue").alias("Total_Revenue"))
category_revenue_df.show()
category_revenue_df.coalesce(1).write.option("header", "true").csv(f"{hdfs_output_path}/e_category_revenue/")
