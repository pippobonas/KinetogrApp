from flask import Flask

def create_app(config,db,migrate):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    return app