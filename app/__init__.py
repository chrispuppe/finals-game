from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_debugtoolbar import DebugToolbarExtension
# from flask_bootstrap import Bootstrap
# Create an Instance of Flask
app = Flask(__name__)
# Include config from config.py
app.config.from_object('config')
app.config['SECRET_KEY'] = secrets.token_urlsafe(24)
# app.secret_key = 's4asdgfkjagh2345nnlqnexiIS9732KksdnsdklkLKJjlksdfJLDF02418'
# Create an instance of SQLAclhemy
db = SQLAlchemy(app)
# Bootstrap(app)
toolbar = DebugToolbarExtension(app)

from app import views, models