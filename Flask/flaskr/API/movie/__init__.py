from flask_cors import CORS
from flaskr.API.movie.movie_list import movie_list
from flaskr.API.movie.movie_search import movie_search

def movie_routes(app):

    CORS(app, resources={r"/moviesList": {"origins": "http://localhost:3000"}})
    @app.route('/moviesList')
    def moviesList():
        return movie_list()
    
    CORS(app, resources={r"/searchMovie": {"origins": "http://localhost:3000"}})
    @app.route('/searchMovie', methods=['POST'])
    def searchMovie():
        return movie_search()