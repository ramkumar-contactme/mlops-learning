from flask import Flask, request
import joblib

app = Flask(__name__)

# load the model
modeldata = joblib.load("height-modelv2.pkl")

def predict_height(weight):
    # make prections
    return modeldata.get('model').predict([[weight]])[0]

@app.route("/")
def ver():
    return "Welcome to height prediction docker image"


@app.route("/version")
def version():
    return str(modeldata.get('version'))

@app.route("/info")
def info():
    return str(modeldata)


@app.route("/predict")
def displayform():
    text = """
    <form method='post' action = "/predictheight">
    <input type="number" name="weight"> Weight<br><br>
    <input type="submit" name = "Predict Height">
    </form>"""
    return text

@app.route("/predictheight", methods=["POST"])
def wish2():
    weight = float(request.form.get('weight'))
    return f"The predicted height for the given weight {weight} is {predict_height(weight)}"  


app.run(host='0.0.0.0', port=5000)