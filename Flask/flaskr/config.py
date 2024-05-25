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
    def __repr__(self):
        '''rappresentation of the object used for debugging '''
        temp_repr = ['Config(' +
        'TESTING={self.TESTING}' +
        'SQLALCHEMY_DATABASE_URI={self.SQLALCHEMY_DATABASE_URI}' +
        'SQLALCHEMY_TRACK_MODIFICATIONS={self.SQLALCHEMY_TRACK_MODIFICATIONS}' +
        ')']
        return temp_repr[0]
    def __str__(self):
        '''rappresentation of the object used for printing '''
        temp_str = ['Config(\n' +
        'TESTING={self.TESTING}\n' +
        'SQLALCHEMY_DATABASE_URI={self.SQLALCHEMY_DATABASE_URI}\n' +
        'SQLALCHEMY_TRACK_MODIFICATIONS={self.SQLALCHEMY_TRACK_MODIFICATIONS}\n' +
        ')']
        return temp_str[0]
