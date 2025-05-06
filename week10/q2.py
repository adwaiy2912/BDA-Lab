from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler, MinMaxScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import RegressionEvaluator, BinaryClassificationEvaluator
import matplotlib.pyplot as plt
import seaborn as sns

# Start a Spark session
spark = SparkSession.builder.appName("EmployeePrediction").getOrCreate()

# a) Load and preprocess employee data from HDFS
# Replace 'hdfs_path' with your actual path
data = spark.read.csv("employee_promotion.csv", header=True, inferSchema=True)

# Show the first few rows to understand the data
data.show()

# Preprocess categorical columns: Use StringIndexer to convert categorical columns to numeric
categorical_columns = ['Department', 'Education']

# Create indexers for each categorical column
indexers = [StringIndexer(inputCol=col, outputCol=col + "_index") for col in categorical_columns]

# Apply StringIndexers
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=indexers)
data = pipeline.fit(data).transform(data)

# Assemble features into a vector
feature_columns = ['Age', 'WorkExperience', 'PerformanceRating', 'TrainingHours', 'Department_index', 'Education_index']
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
data = assembler.transform(data)

# Scale features
scaler = MinMaxScaler(inputCol="features", outputCol="scaled_features")
data = scaler.fit(data).transform(data)

# b) Perform Exploratory Data Analysis (EDA)
# Summary statistics
data.describe().show()

# Visualizing the correlation between features
# Convert DataFrame to Pandas for visualization
pandas_df = data.select("Age", "WorkExperience", "PerformanceRating", "TrainingHours").toPandas()

# Plot correlations
plt.figure(figsize=(10, 6))
sns.heatmap(pandas_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Features")
plt.show()

# c) Build a classification model to predict employee promotion status
# Split the data into train and test
train_data, test_data = data.randomSplit([0.8, 0.2], seed=123)

# Logistic Regression for classification
lr = LogisticRegression(featuresCol='scaled_features', labelCol='PromotionStatus')
lr_model = lr.fit(train_data)

# Predictions on test data
lr_predictions = lr_model.transform(test_data)

# Evaluate the classification model
binary_evaluator = BinaryClassificationEvaluator(labelCol="PromotionStatus")
classification_auc = binary_evaluator.evaluate(lr_predictions)
print(f"Classification AUC: {classification_auc}")

# d) Train a regression model to predict employee salary (Salary)
# For salary prediction, we use Linear Regression
lr_salary = LinearRegression(featuresCol='scaled_features', labelCol='Salary')
salary_model = lr_salary.fit(train_data)

# Predictions on test data
salary_predictions = salary_model.transform(test_data)

# Evaluate the regression model
regression_evaluator = RegressionEvaluator(labelCol="Salary")
rmse = regression_evaluator.evaluate(salary_predictions)
print(f"Regression RMSE: {rmse}")

# e) Visualize insights from models and evaluate performance

# Plot the predicted vs actual values for salary predictions
plt.figure(figsize=(8, 6))
plt.scatter(salary_predictions.select("Salary").toPandas(), salary_predictions.select("prediction").toPandas(), alpha=0.5)
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Actual vs Predicted Salary (Regression)")
plt.show()

# Plot the ROC curve for classification model
from pyspark.ml.evaluation import BinaryClassificationEvaluator
fpr, tpr, thresholds = binary_evaluator.getMetrics(lr_predictions)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2)
plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Logistic Regression")
plt.show()

# Stop the Spark session
spark.stop()

