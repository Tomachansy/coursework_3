from http import HTTPStatus

from flask_restx import Resource, Namespace, reqparse

from app.implemented import movie_service
from app.dao.models.movie import MovieSchema

movies_ns = Namespace('movies')

parser = reqparse.RequestParser()
parser.add_argument("page", type=int)
parser.add_argument("status", type=str)


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.response(int(HTTPStatus.OK), 'OK')
    def get(self):
        """Get all movies"""
        req_args = parser.parse_args()

        if any(req_args.values()):
            filtered_movies = movie_service.get_filter_movies(req_args)
            return MovieSchema(many=True).dump(filtered_movies), HTTPStatus.OK
        else:
            movies = movie_service.get_all()
            return MovieSchema(many=True).dump(movies), HTTPStatus.OK


@movies_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    @movies_ns.response(int(HTTPStatus.OK), 'OK')
    @movies_ns.response(int(HTTPStatus.NOT_FOUND), 'Movie not found')
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            movie = movie_service.get_one(movie_id)
            return MovieSchema().dump(movie), HTTPStatus.OK
        except NameError:
            raise HTTPStatus.NOT_FOUND
