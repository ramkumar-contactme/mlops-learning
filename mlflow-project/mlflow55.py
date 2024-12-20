import pandas as pd
import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.autolog()

df=pd.read_csv("mpg.csv")
y=df.MPG
x=df.drop(columns=["MPG",'Origin'])
xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size=0.2, random_state=2)
model = LinearRegression()
model.fit(xtrain, ytrain)