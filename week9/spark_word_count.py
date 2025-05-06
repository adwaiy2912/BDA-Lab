from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Word Count HDFS")

# Define HDFS input and output paths
hdfs_input_path = "hdfs://localhost:9000/user/220968424/lab9/sample.txt"
hdfs_output_path = "hdfs://localhost:9000/user/220968424/lab9/output0/"

# Load text file from HDFS into an RDD
rdd = sc.textFile(hdfs_input_path)

# Perform word count
word_counts = (rdd.flatMap(lambda line: line.split()) # Split lines into words
			.map(lambda word: (word, 1)) # Map each word to (word, 1)
			.reduceByKey (lambda a, b: a + b)) # Reduce by key to count occurrences
			
# Save the result back to HDFS
word_counts.saveAsTextFile(hdfs_output_path)

# Stop SparkContext
sc.stop()
