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

    def __repr__(self):
        '''rappresentation of the object used for debugging '''
        temp_repr = ['Movie(' +
        'id={self.id}' +
        'title={self.title}' +
        'director={self.director}' +
        'plot={self.plot}' +
        'release_year={self.release_year}' +
        'poster_path={self.poster_path}' +
        'services_available={self.services_available}' +
        ')']
        return temp_repr[0]
    def __str__(self):
        '''rappresentation of the object used for printing '''
        temp_str = ['Movie(\n' +
        'id={self.id}\n' +
        'title={self.title}\n' +
        'director={self.director}\n' +
        'plot={self.plot}\n' +
        'release_year={self.release_year}\n' +
        'poster_path={self.poster_path}\n' +
        'services_available={self.services_available}\n' +
        ')']
        return temp_str[0]
