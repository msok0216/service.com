import os
from datetime import timedelta
from flask import Flask
from flask_session import Session


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    server_session = Session(app)
        # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
        # load the test config if passed in

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    # @app.route('/', methods=('GET', 'PUT'))
    # def hello():
    #     return {'message': 'Hello, World!'}

    from .models.base import db
    from .models.Project import Project
    from .models.Users import Users

    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import user
    app.register_blueprint(user.bp)
    server_session = Session(app)
    with app.app_context():
        from .data_generation import DataGenerator
        DataGenerator(30, 0, 120, 0, 00)
    
    return app

