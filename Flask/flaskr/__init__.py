from .app import create_app
from .config import Config
from .db import db, migrate
from .rest_api import movie_routes

app=create_app(Config,db,migrate)
movie_routes(app)