import secrets
import os

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
SECRET_KEY = secrets.token_urlsafe(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False
WHOOSH_BASE = "whoosh"
# PostgreSQL
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

