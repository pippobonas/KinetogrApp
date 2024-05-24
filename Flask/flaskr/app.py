'''module to create the flask app and return it'''
from flask import Flask

def create_app(config,db,migrate):
    '''
    function to create the flask app
    parameters:
    config: configuration object for the app
    db: database object for the app
    migrate: migration object for the app
    
    if the parameters are None, the app will be created with default configuration:
    - TESTING = False
    - SQLALCHEMY_TRACK_MODIFICATIONS = False
    '''
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
    else:
        app.config['TESTING'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['WTF_CSRF_ENABLED'] = False
    if db is not None:
        db.init_app(app)
        if migrate is not None:
            migrate.init_app(app, db)
    return app
