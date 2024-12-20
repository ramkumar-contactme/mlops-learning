from flask import Flask, request
app=Flask(__name__)
@app.route("/")
def displayform():
    output = """
    <form method="post", action="/predict" >
    <input type=text name=number1> Enter number1<br>
    <input type=text name=number2> Enter number2<br>
    <input type=submit>
    </form>
            """
    return output

@app.route("/predict", methods=["POST"])
def predict():
    num1 = float(request.form.get('number1'))
    num2 = float(request.form.get('number2'))
    return str(num1 + num2)

app.run()