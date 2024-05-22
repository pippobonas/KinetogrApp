from app import create_app
from config import Config
from db import db, migrate

app=create_app(Config,db,migrate)