#manual salary prediction
from flask import Flask, request
app=Flask(__name__)
@app.route("/")
def displayform():
    output = """
    <form method="post", action="/predict" >
    <input type=text name=years> Enter experience in years<br>
    <input type=submit>
    </form>
            """
    return output

def manual_predict(years):
    #y=mx+c
    m=9449.96232146
    c=25792.20019866871
    salary=(m*years) + c
    return salary
    
    # model = joblib.load("height-modelv2.pkl")
    result = model.predict([[ float(weight)]])[0]
    # return str(int(result))
    return f"The result is {round(result)} for {height} height"

@app.route("/predict", methods=["POST"])
def predict():
    years = float(request.form.get('years'))
    
    return f"The predicted salary is {manual_predict(years)}"

app.run()