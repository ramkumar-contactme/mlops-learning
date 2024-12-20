import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

df=pd.read_csv("Salary_Data.csv")
y = df.Salary # output, target
X = df.drop(columns=['Salary']) # input, features
# Generate some random data
# np.random.seed(42)
# X = np.random.rand(100, 1) * 10
# y = 2.5 * X.squeeze() + np.random.randn(100) * 2.5

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Start an MLflow run
with mlflow.start_run():

    # Create a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = model.score(X_test, y_test)

    # Log parameters and metrics to MLflow
    mlflow.log_param("data_size", len(X))
    mlflow.log_param("test_size", 0.2)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # Log the sklearn model
    mlflow.sklearn.log_model(model, "linear_regression_model_on_salary_data")

