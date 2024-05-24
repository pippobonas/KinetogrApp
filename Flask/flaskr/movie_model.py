'''
this class is used to define a model for the movie table in the database.
'''
from flaskr.db import db

class Movie(db.Model):
    '''
    this class have the attributes of the movie
    table_name: movies
    id: primary key
    title: movie title
    director: movie director
    plot: movie plot
    release_year: movie release year
    poster_path: movie poster path 
    services_available: movie services available 
    '''
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    director = db.Column(db.String(128), nullable=False)
    plot = db.Column(db.Text, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    poster_path = db.Column(db.String(4096))
    services_available = db.Column(db.String(64), nullable=False)
