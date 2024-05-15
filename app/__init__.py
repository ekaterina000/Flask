import os
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask_bootstrap import Bootstrap5

from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = "hard to unlock"
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['MAIL_SERVER'] ='smtp.googlemail.com'
flask_app.config['MAIL_PORT'] =587
flask_app.config['MAIL_USE_TLS'] = True
flask_app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
flask_app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

bootstrap = Bootstrap5(flask_app)
db = SQLAlchemy(flask_app)
mail = Mail(flask_app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username