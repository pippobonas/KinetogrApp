from .app import create_app
from .config import Config
from .db import db, migrate
from .rest_api import movie_routes

'''initialize the server with the configuration and the database,migration
    and start the routes movie'''
app=create_app(Config,db,migrate)
movie_routes(app)
