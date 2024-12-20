# logging
from flask import Flask
import joblib
import psutil
from time import ctime,time

LOGFILE = "salary_log.txt"
app=Flask(__name__)
salarymodel = joblib.load("mymodel1.pkl")
print("Salary model loaded")
model_version=3.2
def log(*args):
    textlist = [str(x) for x in args]
    logtext = ",".join(textlist)
    with open(LOGFILE,'a') as f:
        f.write(logtext + '\n')
@app.route("/test")
def test():
    result=[]
    known_inputs=[6,7,8]
    known_outputs=[ 82491.9741274 ,  91941.93644885, 101391.89877031]
    for myinput, myoutput in zip(known_inputs,known_outputs):
        predicted_output=salarymodel.predict([[ myinput]])[0]
        result.append(round(myoutput,5) == round(predicted_output,5))
        print(myoutput,predicted_output)
    return str(result)
@app.route('/predict/<years>')
def compute(years):
    start=time()
    salary = salarymodel.predict([[ float(years)]])[0]
    end=time()
    latency=end-start
    log(ctime(),years,salary,model_version,latency,psutil.cpu_percent(),psutil.virtual_memory().percent)
    return f"The salary is {round(salary)} for {years} years of experience.<br>Time taken : {latency}"
app.run(host='0.0.0.0', port=5000)