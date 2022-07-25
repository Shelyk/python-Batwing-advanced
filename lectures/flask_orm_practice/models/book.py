from database import db


class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_book = db.Column(db.String(300), nullable=False)
    author_book = db.Column(db.String(300), nullable=False)