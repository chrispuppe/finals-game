from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
import os

# Create an Instance of Flask
app = Flask(__name__)

# Include config from config.py
on_heroku = False
if os.environ['IS_ON_HEROKU_ENVIRONMENT']:
  on_heroku = True
  print('Using Heroku environment')
if not on_heroku:
    app.config.from_object('config')
else:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    print('SQLALCHEMY_DATABASE_URI')

# Create an instance of SQLAclhemy
db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)

# from app import views, models