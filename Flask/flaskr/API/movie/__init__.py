from flask_cors import CORS
from flaskr.API.movie.movie_list import movie_list

def movie_routes(app):

    CORS(app, resources={r"/moviesList": {"origins": "http://localhost:3000"}})
    @app.route('/moviesList')
    def moviesList():
        return movie_list()