import http
from flask import Blueprint, Response, request
from db.db import UserDB

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = db.get_all()
    return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return user


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    new_user = db.add(name, email, password)
    return new_user, http.HTTPStatus.CREATED


@user_router.route('', methods=['PUT'])
def update():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    update_user = db.update_by_email(name, email, password)
    if update_user is None:
        return 'A user with this email not found.', http.HTTPStatus.BAD_REQUEST
    return update_user, http.HTTPStatus.ACCEPTED


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    erase = db.delete_by_email(email)
    return erase