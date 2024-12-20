from flask import Flask, request
import joblib
salarymodel = joblib.load("iris.pkl")
print("Salary model loaded")

app=Flask(__name__)
@app.route("/")
def displayform():
    output = """
    <form method="post", action="/predict" >
    <input type=text name=input1> Enter years of experience<br>
    <input type=text name=input2> Enter years of experience<br>
    <input type=text name=input3> Enter years of experience<br>
    <input type=text name=input4> Enter years of experience<br>
    <input type=submit>
    </form>
            """
    return output

@app.route("/predict", methods=["POST"])
def predict():
    input1 = float(request.form.get('input1'))
    input2 = float(request.form.get('input2'))
    input3 = float(request.form.get('input3'))
    input4 = float(request.form.get('input4'))
    salary = salarymodel.predict([[input1, input2, input3, input4]])[0]
    return f"The salary is {(salary)} "
app.run()