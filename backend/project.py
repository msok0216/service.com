from user import token_required
import jwt
import sys, traceback
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, Response, current_app as app
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db

bp = Blueprint('project', __name__, url_prefix='/project/')


@bp.route('/create', methods=['PUT'])
@token_required
def create():
    data = request.get_json()
    db = get_db()

    name = data['name']
    location = data['location']
    manager = data['manager']
    description = data['description']
    hours = data['hours']

    response = {'message': ''}


    try:
        db.execute(
            "INSERT INTO user VALUES (?, ?, ?, ? ?)",
            (name, location, manager, description, hours),
        )
        db.commit()
    except db.Error as error:
        response['message'] = "An error occurred while registering the project"
        print(error.args)
        print(error.__class__)
        type, value, tb = sys.exc_info()
        print(traceback.format_exception(type, value, tb))
    else:
        response['message'] = "Your project is registered"
        db.close()
        return response, 201
    db.close()
    return response, 400



@bp.route('/edit', methods=['PUT'])
@token_required
def edit():  
    data = request.get_json()
    db = get_db()
    id = data['id']
    name = data['name']
    location = data['location']
    manager = data['manager']
    description = data['description']
    hours = data['hours']

    response = {'message': ''}

    try:
        db.execute(
            "UPDATE projects SET name = ?, location = ?, manager = ?, description, = ?, hours = ? WHERE project_id = ?",
            (name, location, manager, description, hours, id),
        )
        db.commit()
    except db.Error as error:
        response['message'] = "An error occurred while updating the project"
        print(error.args)
        print(error.__class__)
        type, value, tb = sys.exc_info()
        print(traceback.format_exception(type, value, tb))
    else:
        response['message'] = "Your project is updated"
        db.close()
        return response, 201
    db.close()
    return response, 400


@bp.route('/delete', methods=['DELETE'])
@token_required
def delete():  
    data = request.get_json()
    db = get_db()

    id = data['id']

    response = {'message': ''}
    try:
        db.execute(
            "DELETE FROM projects WHERE project_id = ?",
            (id),
        )
        db.commit()
    except db.Error as error:
        response['message'] = "An error occurred while deleting the project"
        print(error.args)
        print(error.__class__)
        type, value, tb = sys.exc_info()
        print(traceback.format_exception(type, value, tb))
    else:
        response['message'] = "Your project is deleted"
        db.close()
        return response, 201
    db.close()
    return response, 400


@bp.route('/get', methods=['GET'])
@token_required
def delete():  
    data = request.get_json()
    db = get_db()

    name = data['name']

    results = db.execute(
        "SELECT * FROM projects WHERE name = ?",
        (name),
    ).fetchall()
    db.commit()
    db.close()
    return {'data': results}, 400