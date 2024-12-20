from flask import Flask, request
app=Flask(__name__)
import joblib
irismetadata = joblib.load("iris-model-metadata.pkl")
irismodel=irismetadata.get('model')
print("Iris model loaded")

def classify_iris(pw,pl,sw,sl):
    flower = 'Iris-Setosa'
    return irismodel.predict([[sl,sw,pl,pw]])[0]

@app.route("/info")
def meta():
    return str(irismetadata)
@app.route("/")
def displayform():
    output = """
    <form method="post", action="/predict" >
    <input type=text name=pw> Enter Petal Width<br>
    <input type=text name=pl> Enter Petal Length<br>
    <input type=text name=sw> Enter Sepal Width<br>
    <input type=text name=sl> Enter Sepal Length<br>
    <input type=submit>
    </form>
            """
    return output

@app.route("/predict", methods=["POST"])
def predict():
    pw = float(request.form.get('pw'))
    pl = float(request.form.get('pl'))
    sw = float(request.form.get('sw'))
    sl = float(request.form.get('sl'))
    return classify_iris(pw,pl,sw,sl)

app.run()