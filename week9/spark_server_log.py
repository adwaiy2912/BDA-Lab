from pyspark import SparkContext
import re

sc = SparkContext("local", "Log Analysis")

hdfs_input_path = "hdfs://localhost:9000/user/220968424/lab9/server_log.txt"
hdfs_output_path = "hdfs://localhost:9000/user/220968424/lab9/output1/"

# a) Read the server log file from HDFS into an RDD
log_file_rdd = sc.textFile(hdfs_input_path)

# b) Extract HTTP status codes and count occurrences
def extract_status_code(log_line):
    match = re.search(r'" (\d{3}) ', log_line)
    if match:
        return match.group(1)
    return None

status_codes_rdd = log_file_rdd.map(extract_status_code).filter(lambda x: x is not None)
status_count = status_codes_rdd.map(lambda code: (code, 1)).reduceByKey(lambda a, b: a + b)
status_count.collect()

# c) Find the most common IP addresses accessing the server
def extract_ip(log_line):
    match = re.search(r'^(\d+\.\d+\.\d+\.\d+)', log_line)
    if match:
        return match.group(1)
    return None

ip_rdd = log_file_rdd.map(extract_ip).filter(lambda x: x is not None)
ip_count = ip_rdd.map(lambda ip: (ip, 1)).reduceByKey(lambda a, b: a + b)
top_ips = ip_count.takeOrdered(10, key=lambda x: -x[1])

# d) Filter out error logs (HTTP 4xx and 5xx) and count them.
def is_error_log(log_line):
    match = re.search(r'" (\d{3}) ', log_line)
    if match:
        status_code = int(match.group(1))
        return 400 <= status_code < 600
    return False

error_logs_rdd = log_file_rdd.filter(is_error_log)
error_count = error_logs_rdd.count()

# e) Write the results back to HDFS.
status_count.saveAsTextFile(f"{hdfs_output_path}/b_status_count/")
sc.parallelize(top_ips).saveAsTextFile(f"{hdfs_output_path}/c_top_ips/")
error_logs_rdd.saveAsTextFile(f"{hdfs_output_path}/d_error_logs/")

# Stop SparkContext
sc.stop()
