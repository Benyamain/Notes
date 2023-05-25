from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

database = SQLAlchemy()
DATABASE_NAME = 'notes.db'

def create_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = 'ijfewoijfewifjwievweiofwoiccc'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    database.init_app(app)

    from .views import views
    from .auth import auth

    # No prefix
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    # Import the file so that these classes are defined
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    # Where should we go if user is not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Look for the primary key and check id parameter to see
    # if they match
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DATABASE_NAME):
        with app.app_context():
            database.create_all()

        print('Created database!')