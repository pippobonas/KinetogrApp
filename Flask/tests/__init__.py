'''
- set path /../flaskr to sys.path for import modules from flaskr
- setting fixtures for testing
'''
import sys
import os
import pytest
from flask import Flask
from .configtest import TestConfig as conf

#setting path
current_directory = os.path.dirname(os.path.realpath(__file__))
flaskr_directory = os.path.dirname(current_directory+'/../flaskr')
sys.path.append(current_directory)
sys.path.append(flaskr_directory)

#fixtures
@pytest.fixture(scope='session')
def app ():
    '''
    fixture for flask app
    -dont have anthing
    '''
    app = Flask(__name__)
    app.config.from_object(conf)
    return app

@pytest.fixture(scope='session')
def client(app):
    '''
    fixture for flask client
    '''
    return app.test_client()
