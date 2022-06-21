from app import app
from flask import render_template


@app.route('/')
def hello_world():
    a = 'Hello, my friend from the Cursor!'
    return render_template('index.html', variable=a)


@app.route("/adding/<num1>/<num2>")
def adding(num1, num2):
    result = int(num1) + int(num2)
    return render_template('index.html', variable=result)