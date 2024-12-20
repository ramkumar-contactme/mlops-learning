from flask import Flask, request
import joblib
salarymodel = joblib.load("mymodel1.pkl")
print("Salary model loaded")

app=Flask(__name__)
@app.route("/")
def displayform():
    output = """
    <form method="post", action="/predict" >
    <input type=text name=years> Enter years of experience<br>
    <input type=submit>
    </form>
            """
    return output

@app.route("/predict", methods=["POST"])
def predict():
    years = float(request.form.get('years'))
    salary = salarymodel.predict([[ years]])[0]
    return f"The salary is {round(salary)} for {years} years of experience"
app.run()