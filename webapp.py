from flask import Flask, request
import time
import pickle
import joblib
app=Flask(__name__)

@app.route("/")
def hi():
    return "Hello from flask"

@app.route("/contact")
def contact():
    return "Hello this is Ramesh"

@app.route("/ram")
def ram():
    return "Hello this is Ram"

@app.route("/ml1/<inputs>")
def ml1(inputs):
    # values = request.args.get('inputs', '')
    # arrayInput = values.split(',')
    f=open("iris.pkl",'rb')
    model = pickle.load(f)
    f.close()
    # result = model.predict([[3.4,4.3,4.5,2.3]])
    result = model.predict([inputs])
    return result[0]

@app.route("/ml2/<number>")
def ml2(number):
    
    f=open("mymodel1.pkl",'rb')
    salarymodel = pickle.load(f)
    f.close()
    result = salarymodel.predict([[float(number)]])
    return str(int(result[0]))


@app.route("/ml3/<weight>")
def ml3(weight):
    
    # f=open("height-modelv2.pkl",'rb')
    # model = pickle.load(f)
    # f.close()
    
    model = joblib.load("height-modelv2.pkl")
    result = model.predict([[ float(weight)]])[0]
    # return str(int(result))
    return f"The result is {round(result)} for {height} height"

app.run()