from http import HTTPStatus

from flask_restx import Resource, Namespace

from app.implemented import genre_service
from app.dao.models.genre import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.response(int(HTTPStatus.OK), 'OK')
    @genres_ns.response(int(HTTPStatus.NOT_FOUND), 'Genres not found')
    def get(self):
        """Get all genres"""
        all_genres = genre_service.get_all()

        if all_genres:
            genres_schema = GenreSchema(many=True)
            return genres_schema.dump(all_genres), HTTPStatus.OK
        else:
            raise HTTPStatus.NOT_FOUND


@genres_ns.route('/<int:id>/')
class GenreView(Resource):
    @genres_ns.response(int(HTTPStatus.OK), 'OK')
    @genres_ns.response(int(HTTPStatus.NOT_FOUND), 'Genre not found')
    def get(self, genre_id: int):
        """Get genre by id"""
        genre = genre_service.get_one(genre_id)

        if genre:
            genre_schema = GenreSchema()
            return genre_schema.dump(genre), HTTPStatus.OK
        else:
            raise HTTPStatus.NOT_FOUND
