'''
This file contains the configuration for the Flask app.
'''
class Config:
    '''
    It sets the database URI to a local SQLite database and
    disables the modification tracking feature of SQLAlchemy.
    '''
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///KinetogrApp.db?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
