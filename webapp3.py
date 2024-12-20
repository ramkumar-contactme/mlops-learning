from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/ml1", methods=["GET"])
def ml1():
    # Get the query parameter 'inputs' and split it into a list of floats
    inputs = request.args.get('inputs', '')
    inputs = [float(i) for i in inputs.split(',')]
    
    # Load the model
    with open("iris.pkl", 'rb') as f:
        model = pickle.load(f)

    # Ensure inputs are in the correct format
    result = model.predict([inputs])

    return str(result[0])

if __name__ == "__main__":
    app.run(debug=True)
