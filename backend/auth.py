import functools
import jwt
import datetime
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, Response, current_app as app
)
from .models.Users import Users
from sqlalchemy.exc import IntegrityError

from werkzeug.security import check_password_hash, generate_password_hash

from .models.base import db

bp = Blueprint('auth', __name__, url_prefix='/')


@bp.route('/register', methods=['PUT'])
def register():
    if request.method == 'PUT':
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        confirmPassword = request.get_json()['confirmPassword']
        response = {'error': None}
        if not username:
            response['error'] = 'Username is required'
        elif not email:
            response['error'] = 'Email is required.'
        elif not password:
            response['error'] = 'Password is required.'
        elif not confirmPassword or confirmPassword != password:
            response['error'] = 'Your passwords do not match'
        if response['error'] is None:
            user = Users(username, email, generate_password_hash(password))
            # print(user)
            try:
                print(user)
                db.session.add(user)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                response['error'] = f"This email is already registered."
                return response, 400
            else:
                response['error'] = "Your account is registered"
                return response, 201
    return response, 400



@bp.route('/login', methods=['PUT', 'POST'])
def login():
    if request.method == 'PUT' or request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']
        error = None
        user = Users.getUser(username)
        if user is None:
            error = 'Incorrect Username.'
        elif not check_password_hash(user.Users.getPassword(),password):
            error = 'Incorrect Password.'

        if error is not None:
            # session.clear()
            # session['username'] = user['username']
            print(error)
            return '{ error:' + error + '}', 400
        print(username)
        token = jwt.encode({'user': username}, app.config['SECRET_KEY'])
        session[username] = token
    # return render_template('auth/login.html')
    # print(request)
    return {'token': token, 'username': username}, 200



# @bp.before_app_request
# def load_logged_in_user():
#     username = session.get('username')

#     if username is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()
#     print(username)



@bp.route('/logout', methods=['PUT'])
def logout():
    message = ''
    try:
        token = request.headers.get('token')
        username = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['username']
        session.pop(username)
        message = "User successfully logged out"
    except:
        message = "An error occurred while logging out"
    # if session.
    # session.pop('username')
    return {'message': message}, 200