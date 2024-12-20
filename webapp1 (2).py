from flask import Flask
import joblib
app=Flask(__name__)
salarymodel = joblib.load("mymodel1.pkl")
print("Salary model loaded")
@app.route('/predict/<years>')
def compute(years):
    salary = salarymodel.predict([[ float(years)]])[0]
    return f"The salary is {round(salary)} for {years} years of experience"
app.run()