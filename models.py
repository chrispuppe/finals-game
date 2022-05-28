# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
from __init__ import db
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
    user_id = db.Column(
                            db.Integer, 
                            ForeignKey('user.user_id'), 
                            nullable=False
                            )
    game_date = db.Column(
                            db.String(80), 
                            nullable=False
                            )
    selected_player = db.Column(db.String(80), nullable=False)

    def __init__(self, user_id, game_date, 
                selected_player):
        self.user_id = user_id
        self.game_date = game_date
        self.selected_player = selected_player

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    chris = User(
                    username='Chris', 
                    email='chrispuppe@gmail.com', 
                    password='passowrd'
                    )
    todd = User(
                    username='Todd', 
                    email='tb@gmail.com', 
                    password='passowrd'
                    )
    anddrew = User(
                    username='Andrew', 
                    email='as@gmail.com', 
                    password='passowrd'
                    )
    jake = User(
                    username='Jake', 
                    email='jo@gmail.com', 
                    password='passowrd'
                    )

    ryan = User(
                    username='Ryan', 
                    email='ryan@gmail.com', 
                    password='passowrd'
    )

    foram = User(
                    username='Foram', 
                    email='foram@gmail.com', 
                    password='passowrd'
    )

    mark = User(
                    username='Mark', 
                    email='mark@gmail.com', 
                    password='passowrd'
    )

    tyler = User(
                    username='Tyler', 
                    email='Tyler@gmail.com', 
                    password='passowrd'
    )

    db.session.add(chris)
    db.session.add(todd)
    db.session.add(anddrew)
    db.session.add(jake)
    db.session.add(ryan)
    db.session.add(foram)
    db.session.add(mark)
    db.session.add(tyler)

    db.session.commit()