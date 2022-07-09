from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return 'You can find out my name at "/name"!'


@app.route("/name")
def hello():
    return "Yurii Shelyk"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
