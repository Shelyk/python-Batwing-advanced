from flask import Flask
from config import Config
from database import db
from api.book_api import book_router


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(book_router)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
