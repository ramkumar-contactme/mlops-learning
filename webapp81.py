# logging
from flask import Flask
import joblib
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
    
    
@app.route('/predict/<years>')
def compute(years):
    start=time()
    salary = salarymodel.predict([[ float(years)]])[0]
    end=time()
    latency=end-start
    log(ctime(),years,salary,model_version,latency)
    return f"The salary is {round(salary)} for {years} years of experience.<br>Time taken : {latency}"
app.run()