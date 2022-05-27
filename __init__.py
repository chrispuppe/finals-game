from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

# Create an Instance of Flask
app = Flask(__name__)
# Include config from config.py
app.config.from_object('config')

# Create an instance of SQLAclhemy
db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)

# from app import views, models