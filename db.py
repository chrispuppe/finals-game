# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from config import SQLALCHEMY_DATABASE_URI
from flask.cli import FlaskGroup
from app import app
from run import app
from app import db

cli = FlaskGroup(app)



if __name__ == '__main__':
    cli()