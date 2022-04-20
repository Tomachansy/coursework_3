from http import HTTPStatus

from flask_restx import Namespace, reqparse, Resource

from app.dao.models.favorite_movie import FavoriteMovieSchema
from app.helpers.decorators import auth_required
from app.implemented import fav_movie_service

favorite_movies_ns = Namespace('favorites')

parser = reqparse.RequestParser()
parser.add_argument("page", type=int)
parser.add_argument("status", type=str)


@favorite_movies_ns.route('/movies/')
class FavoriteMoviesView(Resource):
    @auth_required
    @favorite_movies_ns.response(int(HTTPStatus.OK), 'OK')
    @favorite_movies_ns.response(int(HTTPStatus.NOT_FOUND), 'Movies not found')
    def get(self, user_id: int):
        """Get all favorite movies"""
        req_args = parser.parse_args()

        if any(req_args.values()):
            filtered_movies = fav_movie_service.get_filter_movies(req_args, user_id)
            movies = FavoriteMovieSchema(many=True).dump(filtered_movies)

            fav_movies = []
            for movie in movies:
                fav_movies.append(movie["movie"])

            return fav_movies, HTTPStatus.OK

        else:
            movies = FavoriteMovieSchema(many=True).dump(fav_movie_service.get_by_user_id(user_id))

            fav_movies = []
            for movie in movies:
                fav_movies.append(movie["movie"])

            return fav_movies, HTTPStatus.OK


@favorite_movies_ns.route('/movies/<int:movie_id>/')
class FavoriteMoviesView(Resource):
    @auth_required
    @favorite_movies_ns.response(int(HTTPStatus.OK), 'OK')
    @favorite_movies_ns.response(int(HTTPStatus.NO_CONTENT), 'Movies added to the favorite list')
    @favorite_movies_ns.response(int(HTTPStatus.NOT_FOUND), 'Movie not found')
    def post(self, movie_id: int, user_id: int):
        """Add a movie to the favorite list"""
        if movie_id:
            fav_movie_service.create(user_id, movie_id)
            return "", HTTPStatus.NO_CONTENT
        else:
            raise HTTPStatus.NOT_FOUND

    @auth_required
    @favorite_movies_ns.response(int(HTTPStatus.NO_CONTENT), 'Movies removed from the favorite list')
    def delete(self, movie_id: int, user_id: int):
        """Delete a movie from the favorite list"""
        if movie_id:
            fav_movie_service.delete(user_id, movie_id)
            return "", HTTPStatus.NO_CONTENT
        else:
            raise HTTPStatus.NOT_FOUND
