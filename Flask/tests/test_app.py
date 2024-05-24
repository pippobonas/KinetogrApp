'''
This file contains tests for create_app function in app.py
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pytest
from flaskr.app import create_app
from configtest import TestConfig as conf


class Test_create_app:
    '''
    class for testing create_app function
    '''
    setup = [{'db': SQLAlchemy(), 'migrate': Migrate(), 'conf': conf},
             {'db': SQLAlchemy(), 'migrate': Migrate(), 'conf': None},
             {'db': SQLAlchemy(), 'migrate': None, 'conf': conf},
             {'db': SQLAlchemy(), 'migrate': None, 'conf': None},
             {'db': None, 'migrate': Migrate(), 'conf': conf},
             {'db': None, 'migrate': Migrate(), 'conf': None},
             {'db': None, 'migrate': None, 'conf': conf},
             {'db': None, 'migrate': None, 'conf': None}]
    @pytest.mark.parametrize('setup', setup )
    def test_app(self, setup):
        '''
        parametrized test for create_app function
        '''
        app = create_app(conf, setup['db'],setup['migrate'])
        assert app is not None
        assert app.config['TESTING'] == conf.TESTING
        assert app.config['SQLALCHEMY_DATABASE_URI'] == conf.SQLALCHEMY_DATABASE_URI
        assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] == conf.SQLALCHEMY_TRACK_MODIFICATIONS
        assert app.config['WTF_CSRF_ENABLED'] == conf.WTF_CSRF_ENABLED
