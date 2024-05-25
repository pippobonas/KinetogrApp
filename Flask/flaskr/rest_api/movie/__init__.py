'''this method is used to define the routes for the movie module'''
from flask_cors import CORS
from flaskr.rest_api.movie.movie_list import movie_list
from flaskr.rest_api.movie.movie_search import movie_search

def movie_routes(app):
    '''
    The routes are only available from localhost
    Defined the routes:
    - /moviesList
    - /searchMovie
    '''
    #route /moviesList
    CORS(app, resources={r"/moviesList": {"origins": "http://localhost:3000"}})
    @app.route('/moviesList')
    def route_search_movies_list():
        return movie_list()
    #route /searchMovie
    CORS(app, resources={r"/searchMovie": {"origins": "http://localhost:3000"}})
    @app.route('/searchMovie', methods=['POST'])
    def route_search_movie():
        return movie_search()
