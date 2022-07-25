from flask import Blueprint, request, session, redirect, url_for

auth_router = Blueprint("auth", __name__, url_prefix="/auth")


@auth_router.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            session["email"] = email
            return redirect(url_for("auth.profile"))
        return "NONE"

    return """
        <form method="POST">
            <label for="password">Email</label>"
            <input name="email" type="text"/> 
            <label for="password">Password</label>"
            <input name="password" type="password"/>
            <button type="submit">Login</button>x`
        <form/>
    """


@auth_router.route('/profile', methods=['GET'])
def profile():
    if  email := session.get('email'):
        return f"WELCOME {email}"
    else:
        return f"Please login"


@auth_router.route('/logout', methods=['GET'])
def logout():
    session.pop('email')
    return "Successfully logged aut"