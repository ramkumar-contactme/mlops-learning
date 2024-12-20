from flask import Flask
import time

app=Flask(__name__)

@app.route("/")
def hi():
    return "Hello from flask"

@app.route("/contact")
def contact():
    return "Hello this is Ramesh"

@app.route("/now")
def now():
    return time.ctime()

@app.route("/hi/<name>")
def abcd(name):
    return  f"Hello {name}"

@app.route("/square/<number>")
def square(number):
    return  number * number




app.run()