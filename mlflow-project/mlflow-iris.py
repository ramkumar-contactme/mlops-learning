import pandas as pd
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.autolog()

df=pd.read_csv("iris.csv")
y = df.Species # output, target
x = df.drop(columns=['Species','Id']) # input, features
xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size=0.2, random_state=2)
model = LogisticRegression()
model.fit(xtrain, ytrain)