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

def new_selection():
    selected_info = Selection(
                                user_id=1,
                                game_date='MAY 20, 2022',
                                selected_player='Stephen Curry',
                                user_selection_order=1
    )
    db.session.add(selected_info)
    db.session.commit()

db.drop_all() # make sure to remove this in production
db.create_all()

chris = User(username='Chris', email='chrispuppe@gmail.com')
todd = User(username='Todd')
anddrew = User(username='Andrew')
jake = User(username='Jake')



db.session.add(chris)
db.session.add(todd)
db.session.add(anddrew)
db.session.add(jake)

# db.session.add(new_selection)

db.session.commit()
