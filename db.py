# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Programming/db/FinalsGame.db'
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Selection(db.Model):
    selection_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)
    game_date = db.Column(db.String(80), unique=True, nullable=False)
    selected_player = db.Column(db.String(80), unique=True, nullable=False)
    user_selection_order = db.Column(db.Integer, nullable=False)

db.drop_all() # make sure to remove this in production
db.create_all()

