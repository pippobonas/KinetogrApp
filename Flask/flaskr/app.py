from flask import Flask

def create_app(config,db,migrate):
    app = Flask(__name__)
    if(config != None):
        app.config.from_object(config)
    else:
        app.config['TESTING'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kine.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['WTF_CSRF_ENABLED'] = False
    if db != None:
        db.init_app(app)
        if migrate != None:
            migrate.init_app(app, db)
    
    
    return app