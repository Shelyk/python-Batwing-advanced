import http

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from user_api import user_router


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


app.register_blueprint(user_router)

@app.route('/')
def index():
    return "hello world0"

@app.errorhandler(404)
def handle_404(e):
    return 'Sorry, this resource does not exist', http.HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    print(db)
    app.run(host="0.0.0.0")