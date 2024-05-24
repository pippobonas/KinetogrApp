'''
module for configuration of flask
'''
class TestConfig:
    '''
    default clas configuration for testing
    '''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
