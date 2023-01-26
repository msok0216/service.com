from functools import wraps
import jwt
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, Response, current_app as app
)
from werkzeug.security import check_password_hash, generate_password_hash
from .models.Users import Users
from .models.Shift import Shift
from .models.Likes import Likes
from .models.Connections import Connections
from .models.base import db

bp = Blueprint('user', __name__, url_prefix='/user/')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return {'error':'Invalid Request'}, 401
        try:
            print(token)
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            username = data['user']
            kwargs['username'] = username
            if not session[username]: return {'error': 'Token is invalid'}, 401
        except:
            return {'error': 'Token is invalid'}, 401
        
        return f(*args, **kwargs)
    return decorated


@bp.route('/authenticate', methods=['PUT'])
@token_required
def authenticate():
    return {'message': 'The user is authenticated'}, 200


@bp.route('/likes', methods=['GET'])
@token_required
def getLikes(username):
    likes = Likes.getUsersAllLikes(username)

    return {'likes': likes}, 200

@bp.route('/shifts', methods=['GET'])
@token_required
def getShifts(username):
    page = request.headers.get('page')
    shifts = Shift.getPaginatedShifts(username, page)
    pages = Shift.totalPages(username)
    return {'shifts': shifts, 'pages': pages}, 200
   
@bp.route('/graphdata', methods=['GET'])
@token_required
def getAllShifts(username):
    shifts = Shift.getAllShifts(username)
    return {'shifts': shifts}, 200

@bp.route('/connections', methods=['GET'])
@token_required
def getConnections(username):
    connections = Connections.getConnections(username)
    return {'connections': connections}, 200



# @bp.route('/finance/graph', methods=['GET'])
# @token_required
# def graph():
#     response = request.json()
#     username = response['username']
#     start_date = response['start_date']
#     end_date = response['end_date']



#     db = get_db()
#     data = db.execute(
#         'SELECT * FROM finance WHERE username = ? AND purchase_date > ?', 
#             (username, start_date,)
#     ).fetchall()

#     for row in data:



@bp.route('/paginate')
@token_required
def paginate():
    return 1





@bp.route('/post/<user_id>')
@token_required
def todo():
    return 'hello world'


@bp.route('/connections')
@token_required
def k():
    return 'hello world'



@bp.route('/todo/<finance_id>')
@token_required
def logour():
    return 'hello world'
