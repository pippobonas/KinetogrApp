from .app import create_app
from .config import Config
from .db import db, migrate
from .API import movie_routes

app=create_app(Config,db,migrate)
movie_routes(app)