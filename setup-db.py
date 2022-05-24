# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app.models import User, Selection
# from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Programming/db/FinalsGame.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username

class Selection(db.Model):
    selection_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)
    game_date = db.Column(db.String(80), unique=True, nullable=False)
    selected_player = db.Column(db.String(80), unique=True, nullable=False)
    user_selection_order = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, game_date, 
                selected_player, user_selection_order):
        self.user_id = user_id
        self.game_date = game_date
        self.selected_player = selected_player
        self.user_selection_order = user_selection_order


db.drop_all()
db.create_all()

chris = User(username='Chris', email='chrispuppe@gmail.com', password='passowrd')
todd = User(username='Todd', email='tb@gmail.com', password='passowrd')
anddrew = User(username='Andrew', email='as@gmail.com', password='passowrd')
jake = User(username='Jake', email='jo@gmail.com', password='passowrd')

db.session.add(chris)
db.session.add(todd)
db.session.add(anddrew)
db.session.add(jake)

db.session.commit()
