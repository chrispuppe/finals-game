# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
from app import db
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin


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
    game_date = db.Column(db.String(80), nullable=False)
    selected_player = db.Column(db.String(80), nullable=False)

    def __init__(self, user_id, game_date, 
                selected_player):
        self.user_id = user_id
        self.game_date = game_date
        self.selected_player = selected_player
