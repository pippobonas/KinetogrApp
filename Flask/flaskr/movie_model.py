from flaskr.db import db

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    director = db.Column(db.String(128), nullable=False)
    plot = db.Column(db.Text, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    poster_path = db.Column(db.String(4096))
    services_available = db.Column(db.String(64), nullable=False)

