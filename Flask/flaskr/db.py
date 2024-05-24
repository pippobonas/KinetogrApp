'''
this module is used to create the database instance 
and the migration instance
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
