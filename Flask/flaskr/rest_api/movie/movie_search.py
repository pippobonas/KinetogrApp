from flask import jsonify, request
from flaskr.movie_model import Movie

# API endpoint per la ricerca per titolo

def movie_search():
    data = request.json  # Assuming the data is sent as JSON in the request body

    if 'title' not in data:
        return jsonify({"Errore": "campo 'title' mancante"}), 400

    title_search = data['title']

    movies_found = Movie.query.filter_by(title=title_search).all()

    if not movies_found:
        return jsonify({"Errore": "nessun film trovato con il titolo specificato"}), 404

    results = [
        {
            "id": movie.id,
            "title": movie.title,
            "director": movie.director,
            "plot": movie.plot,
            "release_year": movie.release_year,
            "poster_path": movie.poster_path.replace('\\', '/'),
            "services_available": movie.services_available,
        }
        for movie in movies_found
    ]

    return jsonify({"results": results})