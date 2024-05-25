'''initialize and start the server and set routes on'''
from .app import create_app
from .config import Config
from .db import db, migrate
from .rest_api import movie_routes

#initialize the server with the configuration,db,migration '''
app=create_app(Config,db,migrate)

#initialize the routes for the server
movie_routes(app)
