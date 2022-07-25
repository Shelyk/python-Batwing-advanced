from flask import Blueprint, render_template, make_response, request

group_router = Blueprint('group', __name__, url_prefix='/group')


@group_router.route('')
def get():
    groups = [
        {"name": "Cool guys", "id": 1},
        {"name": "Cars", "id": 2},
        {"name": "Flask Rest", "id": 3}
            ]
    return render_template("group.html", groups=groups)

@group_router.route('/<int:id_>')
def retrieve(id_):
    print(id_)
    resp = make_response(render_template("group.html", group_id=id_))
    resp.set_cookie(f'group_id_{id_}', "group")
    return resp

@group_router.route('/<int:id_>/read_cookie')
def read_cookie(id_):
    print(id_)
    if f"group_id_{id_}" in request.cookies:
        return request.cookies.get(f"group_id_{id_}")
    return "no cookie"