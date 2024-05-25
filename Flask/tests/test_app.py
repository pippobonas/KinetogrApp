'''
This file contains tests for create_app function in app.py
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pytest
from flaskr.app import create_app
from tests.configtest import TestConfig as conf


class TestCreateApp:
    '''
    class for testing create_app function
    '''
    setup = [{'db': SQLAlchemy(), 'migrate': Migrate()},
             {'db': SQLAlchemy(), 'migrate': None},
             {'db': None, 'migrate': Migrate()},
             {'db': None, 'migrate': None}]

    @pytest.mark.parametrize('setup', setup )
    def test_app_conf(self, setup):
        '''
        parametrized test for create_app function
        '''
        app = create_app(conf, setup['db'],setup['migrate'])
        assert app is not None
        assert app.config['TESTING'] == conf.TESTING
        assert app.config['SQLALCHEMY_DATABASE_URI'] == conf.SQLALCHEMY_DATABASE_URI
        assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] == conf.SQLALCHEMY_TRACK_MODIFICATIONS
        assert app.config['WTF_CSRF_ENABLED'] == conf.WTF_CSRF_ENABLED
    @pytest.mark.parametrize('setup', setup )
    def test_app_conf_nan(self, setup):
        '''
        parametrized test for create_app function when configuration is None
        '''
        app = create_app(None, setup['db'],setup['migrate'])
        assert app is not None
        assert app.config['TESTING'] is False
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///KinetogrApp.db?charset=utf8'
        assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
        assert app.config['WTF_CSRF_ENABLED'] is False
