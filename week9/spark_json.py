from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("JSON Data Processing").getOrCreate()

# Define HDFS input and output paths
hdfs_input_path = "hdfs://localhost:9000/user/220968424/lab9/json_data.json"
hdfs_output_path = "hdfs://localhost:9000/user/220968424/lab9/output2/"

# a) Read a JSON file from HDFS into a Spark DataFrame.
df = spark.read.json(hdfs_input_path)
df.coalesce(1).write.json(f"{hdfs_output_path}/a_raw_data_json/")
df.show()

# b) Select specific fields (name and city) and save them as JSON.
selected_df = df.select("name", "city")
selected_df.coalesce(1).write.json(f"{hdfs_output_path}/b_selected_data_json/")
selected_df.show()

# c) Filter records based on a condition (e.g., users older than 30).
filtered_df = df.filter(df.age > 30)
filtered_df.coalesce(1).write.json(f"{hdfs_output_path}/c_filtered_data_json/")
filtered_df.show()

# d) Perform a group-by operation on a categorical field (e.g., by city).
grouped_df = df.groupBy("city").count()
grouped_df.coalesce(1).write.json(f"{hdfs_output_path}/d_grouped_data_json/")
grouped_df.show()

