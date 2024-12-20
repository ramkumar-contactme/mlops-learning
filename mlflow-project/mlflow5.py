from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow.sklearn
import numpy as np
import pandas as pd



#mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.autolog()

df=pd.read_csv("mpg.csv")
y = df.MPG # output, target
x = df.drop(columns=['MPG']) # input, features

xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size=0.2, random_state=2)
model = LogisticRegression()
model.fit(xtrain, ytrain)