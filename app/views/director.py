from http import HTTPStatus

from flask_restx import Resource, Namespace

from app.implemented import director_service
from app.dao.models.director import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.response(int(HTTPStatus.OK), 'OK')
    @directors_ns.response(int(HTTPStatus.NOT_FOUND), 'Directors not found')
    def get(self):
        """Get all directors"""
        all_directors = director_service.get_all()

        if all_directors:
            directors_schema = DirectorSchema(many=True)
            return directors_schema.dump(all_directors), HTTPStatus.OK
        else:
            raise HTTPStatus.NOT_FOUND


@directors_ns.route('/<int:id>/')
class DirectorView(Resource):
    @directors_ns.response(int(HTTPStatus.OK), 'OK')
    @directors_ns.response(int(HTTPStatus.NOT_FOUND), 'Director not found')
    def get(self, director_id: int):
        """Get director by id"""
        director = director_service.get_one(director_id)

        if director:
            director_schema = DirectorSchema()
            return director_schema.dump(director), HTTPStatus.OK
        else:
            raise HTTPStatus.NOT_FOUND

