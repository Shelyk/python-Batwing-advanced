from flask_sqlalchemy import SQLAlchemy

from database import db
from models.user import User
from models.book import Book
from main import app
db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.commit()
    print("created tables")