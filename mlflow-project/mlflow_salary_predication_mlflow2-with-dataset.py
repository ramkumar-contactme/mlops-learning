import mlflow
logged_model = 'runs:/65928f0f02084877a3a8e0a304aaaae1/linear_regression_model_on_random_data'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

# data = {'YearsExperience': [1.1,2,3,4,5,7,6]}
import pandas as pd
df = pd.read_csv("Salary_Data.csv")
dfnew = df.drop(columns=['Salary'])
print(loaded_model.predict(pd.DataFrame(dfnew)))