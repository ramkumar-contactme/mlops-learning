from flask import Flask
import joblib
app=Flask(__name__)
heightmodel = joblib.load("height-modelv2.pkl")
print("Salary model loaded")
@app.route('/predict/<weight>')
def compute(weight):
    height = heightmodel.predict([[ float(weight)]])[0]
    return f"The height is {round(height)} for {weight} pounds of weight"
app.run()