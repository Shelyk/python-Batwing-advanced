from app import app
from flask import render_template, request, redirect, jsonify
from helpers.file import get_users, write_users


@app.route('/')
def main_page():
    users = get_users()
    return render_template('index.html', users=users)


@app.route('/user-add')
def user_add():
    return render_template('user-add.html')


@app.route('/users', methods=['POST'])
def save_user():
    users = get_users()

    id = 1
    if len(users) > 0:
        id = len(users) + 1

    user = {
        "id": id,
        'email': request.form.get('email'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'work_area': request.form.get('working_area')
    }

    users.append(user)
    write_users(users)
    return redirect("/")


@app.route("/user-edit/<int:id>")
def edit(id):
    users = get_users()

    for user in users:
        if user["id"] == id:
            return render_template("user-add.html", user=user)

    return redirect("/")


@app.route("/users/<int:id>", methods=["POST"])
def update(id):
    users = get_users()

    for user in users:
        if user["id"] == id:
            user["email"] = request.form.get("email")
            user["first_name"] = request.form.get("first_name")
            user["last_name"] = request.form.get("last_name")
            user["work_area"] = request.form.get("working_area")

    write_users(users)
    return redirect("/")


@app.route("/users/delete/<int:id>")
def delete(id):
    users = get_users()
    del users[id - 1]
    write_users(users)
    return redirect("/")


@app.route("/search", methods=["POST"])
def search():
    res = request.form.get('search')
    res_lower = res.lower()
    users = get_users()
    final_list = []

    if res == '':
        final_list = users
    else:
        for user in users:
            user_str = {str(key): str(val) for key, val in user.items()}
            user_low = {key.lower(): val.lower() for key, val in user_str.items()}
            if res_lower in user_low.values():
                final_list.append(user)

    if len(final_list) < 2:
        result_cnt = 'result'
    else:
        result_cnt = 'results'

    return render_template("search.html", users=final_list, count=len(final_list), result=result_cnt)

