from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)

# Detects the environment local or Heroku
on_heroku = False
if os.environ.get('IS_ON_HEROKU_ENVIRONMENT') is not None:
  on_heroku = True
  print('Using Heroku environment')
if on_heroku == False:
    app.config.from_object('config')
else:
    app.config.from_object('remote_config')

# Create an instance of SQLAclhemy
db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)
