from flask import Flask

from auth_api import auth_router
from config import Config
from database import db
from user_api import user_router
from book_api import book_router
from group_api import group_router

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = "super_secret_key"

    db.init_app(app)
    app.register_blueprint(user_router)
    app.register_blueprint(book_router)
    app.register_blueprint(group_router)
    app.register_blueprint(auth_router)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
