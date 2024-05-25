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
    def __repr__(self):
        '''rappresentation of the object used for debugging '''
        temp_repr = ['Config:[' +
        'TESTING:{self.TESTING},' +
        'SQLALCHEMY_DATABASE_URI:{self.SQLALCHEMY_DATABASE_URI},' +
        'SQLALCHEMY_TRACK_MODIFICATIONS:{self.SQLALCHEMY_TRACK_MODIFICATIONS},' +
        'WTF_CSRF_ENABLED:{self.WTF_CSRF_ENABLED},' +
        ']']
        return temp_repr[0]
    def __str__(self):
        '''rappresentation of the object used for printing '''
        temp_str = ['Config(\n' +
        'TESTING={self.TESTING}\n' +
        'WTF_CSRF_ENABLED={self.WTF_CSRF_ENABLED}\n' +
        'SQLALCHEMY_DATABASE_URI={self.SQLALCHEMY_DATABASE_URI}\n' +
        'SQLALCHEMY_TRACK_MODIFICATIONS={self.SQLALCHEMY_TRACK_MODIFICATIONS}\n' +
        ')']
        return temp_str[0]
