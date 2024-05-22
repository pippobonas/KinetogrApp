from flask import jsonify
from flaskr.movie_model import Movie

def movie_list():
    movies = Movie.query.all()
    if(not movies):
        return jsonify({"Errore": "nessun film trovato"}), 400
    movies_list = [
        {
            'title': movie.title,
            'director': movie.director,
            'plot': movie.plot,
            'release_year': movie.release_year,
            'poster_path': movie.poster_path.replace('\\', '/'),
            'services_available': movie.services_available,
        }
        for movie in movies
    ]

    return jsonify(movies_list)