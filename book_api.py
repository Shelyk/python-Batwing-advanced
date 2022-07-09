import http
from flask import Blueprint, Response, request
from db.books_db import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    return Response(str(books))


@book_router.route('/<string:id>')
def retrieve(id):
    book = db.retrieve(id)
    return book


@book_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    author = request.json.get("author")
    genre = request.json.get("genre")
    id = request.json.get('id')
    new_book = db.add(name, author, genre, id)
    if not new_book:
        return "This book is already exists", http.HTTPStatus.BAD_REQUEST
    else:
        return new_book, http.HTTPStatus.CREATED


@book_router.route('', methods=['PUT'])
def update():
    name = request.json.get("name")
    author = request.json.get("author")
    genre = request.json.get("genre")
    id = request.json.get("id")
    update_user = db.update(name, author, genre, id)

    if not update_user:
        return "This book doesn't exists", http.HTTPStatus.BAD_REQUEST
    else:
        return "Books data has been changed", http.HTTPStatus.CREATED


@book_router.route('/<string:id>', methods=['DELETE'])
def delete(id):
    erase = db.delete(id)
    return erase