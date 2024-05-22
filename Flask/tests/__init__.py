import sys
import os

"""Add the parent directory to the sys.path so that the tests can import the modules from the src directory"""
current_directory = os.path.dirname(os.path.realpath(__file__))
flaskr_directory = os.path.dirname(current_directory+'/../flaskr')

sys.path.append(current_directory)
sys.path.append(flaskr_directory)

import pytest
from configtest import TestConfig as conf
from flask import Flask
#fixtures

@pytest.fixture(scope='session')
def app ():
    app = Flask(__name__)
    app.config.from_object(conf)
    return app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
