import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler, MinMaxScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import RegressionEvaluator, BinaryClassificationEvaluator

# Initialize Spark Session
spark = SparkSession.builder.appName("ML_Spark_HDFS").getOrCreate()

# Load CSV Data from HDFS
df = spark.read.csv("hdfs://localhost:9000/user/220968424/lab10/company_ml_data.csv", header=True, inferSchema=True)

# Perform Basic Data Analysis
print("Dataset Sample:")
df.show(5)
print("Dataset Schema:")
df.printSchema()

# Convert Department (Categorical) into Numeric
indexer = StringIndexer(inputCol="department", outputCol="department_index")
df = indexer.fit(df).transform(df)

# Assemble Features
assembler = VectorAssembler(inputCols=["age", "salary", "experience"], outputCol="features")
df = assembler.transform(df)

# Scale Features
scaler = MinMaxScaler(inputCol="features", outputCol="scaled_features")
df = scaler.fit(df).transform(df)

# Split Data into Train and Test Sets
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

# Train Regression Model (Salary Prediction)
lr = LinearRegression(featuresCol="scaled_features", labelCol="salary")
reg_model = lr.fit(train_df)
reg_predictions = reg_model.transform(test_df)
reg_evaluator = RegressionEvaluator(labelCol="salary", metricName="rmse")
rmse = reg_evaluator.evaluate(reg_predictions)
print("Regression RMSE:", rmse)

# Train Classification Model (Churn Prediction)
classifier = LogisticRegression(featuresCol="scaled_features", labelCol="churn")
clf_model = classifier.fit(train_df)
clf_predictions = clf_model.transform(test_df)
clf_evaluator = BinaryClassificationEvaluator(labelCol="churn")
auc = clf_evaluator.evaluate(clf_predictions)
print("Classification AUC:", auc)

# Train Clustering Model (Employee Segmentation)
kmeans = KMeans(featuresCol="scaled_features", k=3)
kmeans_model = kmeans.fit(df)
kmeans_predictions = kmeans_model.transform(df)
kmeans_predictions.select("employee_id", "prediction").show(5)

# Convert Predictions to Pandas for Visualization
reg_pandas = reg_predictions.select("salary", "prediction").toPandas()
clf_pandas = clf_predictions.select("churn", "prediction").toPandas()
kmeans_pandas = kmeans_predictions.select("employee_id", "prediction").toPandas()

# Visualization - Regression (Actual vs Predicted Salary)
plt.figure(figsize=(8, 5))
plt.scatter(reg_pandas["salary"], reg_pandas["prediction"], alpha=0.5, color="blue", label="Predicted")
plt.plot([reg_pandas["salary"].min(), reg_pandas["salary"].max()],
         [reg_pandas["salary"].min(), reg_pandas["salary"].max()],
         color="red", linestyle="--", label="Perfect Prediction")
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Salary Prediction - Regression")
plt.legend()
plt.show()

# Visualization - Classification (Churn Prediction)
plt.figure(figsize=(6, 4))
plt.hist([clf_pandas["churn"][clf_pandas["prediction"] == 0],
          clf_pandas["churn"][clf_pandas["prediction"] == 1]],
         bins=2, label=["No Churn", "Churn"], color=["blue", "red"])
plt.xticks([0, 1])
plt.xlabel("Actual Churn")
plt.ylabel("Count")
plt.title("Churn Prediction - Classification")
plt.legend()
plt.show()

# Visualization - Clustering (Employee Segments)
plt.figure(figsize=(7, 5))
plt.hist(kmeans_pandas["prediction"], bins=3, color="green", edgecolor="black")
plt.xlabel("Cluster ID")
plt.ylabel("Number of Employees")
plt.title("Employee Segmentation - Clustering")
plt.show()

# Save Models to HDFS
reg_model.save("hdfs://localhost:9000/user/studentregno/lab10/regression_model")
clf_model.save("hdfs://localhost:9000/user/studentregno/lab10/classification_model")
kmeans_model.save("hdfs://localhost:9000/user/studentregno/lab10/kmeans_model")

# Load and Use a Saved Model
from pyspark.ml.classification import LogisticRegressionModel
loaded_clf = LogisticRegressionModel.load("hdfs://localhost:9000/user/studentregno/lab10/classification_model")
new_predictions = loaded_clf.transform(test_df)
new_predictions.select("employee_id", "churn", "prediction").show(5)

# Stop Spark Session
spark.stop()

