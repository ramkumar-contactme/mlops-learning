import pandas as pd
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.autolog()

df=pd.read_csv("diabetes.csv")
y=df.Outcome
x=df.drop(columns=["Outcome"])
xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size=0.2, random_state=2, shuffle=True, stratify=df.Outcome)
model = LogisticRegression()
model.fit(xtrain, ytrain)