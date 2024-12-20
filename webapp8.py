# logging
from flask import Flask
import joblib
from time import ctime
LOGFILE = "salary_log.txt"
app=Flask(__name__)
salarymodel = joblib.load("mymodel1.pkl")
print("Salary model loaded")

def log(*args):
    textlist = [str(x) for x in args]
    logtext = ",".join(textlist)
    with open(LOGFILE,'a') as f:
        f.write(logtext + '\n')
    
    
@app.route('/predict/<years>')
def compute(years):
    salary = salarymodel.predict([[ float(years)]])[0]
    log(ctime(),years)
    return f"The salary is {round(salary)} for {years} years of experience"
app.run()