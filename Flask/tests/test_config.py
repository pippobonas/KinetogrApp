'''
test class Config from Flask/flaskr/config.py
'''
from flaskr.config import Config

class TestConfig:
    '''test class Config '''
    def test_config_repr(self):
        '''test __repr__ method of Config class'''
        config = Config()
        expected_repr=f'Config( TESTING={config.TESTING} ' \
                    f'SQLALCHEMY_DATABASE_URI={config.SQLALCHEMY_DATABASE_URI} ' \
                    f'SQLALCHEMY_TRACK_MODIFICATIONS={config.SQLALCHEMY_TRACK_MODIFICATIONS} )'
        assert repr(config) == expected_repr

    def test_config_str(self):
        '''test __str__ method of Config class'''
        config = Config()
        expected_str = f'Config(\nTESTING={config.TESTING}\n' \
                    f'SQLALCHEMY_DATABASE_URI={config.SQLALCHEMY_DATABASE_URI}\n' \
                    f'SQLALCHEMY_TRACK_MODIFICATIONS={config.SQLALCHEMY_TRACK_MODIFICATIONS}\n)'
        assert str(config) == expected_str

    def test_config_values(self):
        '''test values of Config class'''
        config=Config()
        assert config.TESTING is False
        assert config.SQLALCHEMY_DATABASE_URI == 'sqlite:///KinetogrApp.db?charset=utf8'
        assert config.SQLALCHEMY_TRACK_MODIFICATIONS is False
