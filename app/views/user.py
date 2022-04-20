from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource

from app.dao.models.user import UserSchema
from app.helpers.decorators import auth_required
from app.implemented import user_service, auth_service

users_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    @auth_required
    @users_ns.response(int(HTTPStatus.OK), 'OK')
    @users_ns.response(int(HTTPStatus.BAD_REQUEST), 'Invalid json message received')
    @users_ns.response(int(HTTPStatus.NOT_FOUND), 'User not found')
    def get(self, user_id: int):
        """Get users profile"""

        if user_id:
            user = user_service.get_one(user_id)
            response = UserSchema().dump(user)

            return response, HTTPStatus.OK

        if not user_id:
            raise HTTPStatus.BAD_REQUEST
        else:
            raise HTTPStatus.NOT_FOUND

    @auth_required
    @users_ns.response(int(HTTPStatus.NO_CONTENT), 'User information changed')
    def patch(self, user_id: int):
        """Change users information"""
        data = request.json
        if data:
            user = user_service.get_one(user_id)
            data["id"] = user_id
            UserSchema().dump(user_service.update_user(data, user))

            return "", HTTPStatus.NO_CONTENT

        if not data:
            raise HTTPStatus.BAD_REQUEST
        else:
            raise HTTPStatus.NOT_FOUND


@users_ns.route('/password/')
class UserPatchView(Resource):
    @auth_required
    @users_ns.response(int(HTTPStatus.OK), 'OK')
    @users_ns.response(int(HTTPStatus.NO_CONTENT), 'Password changed')
    @users_ns.response(int(HTTPStatus.BAD_REQUEST), 'Invalid json message received')
    def put(self, user_id: int):
        """Change users password"""
        data = request.json

        if data:
            user = user_service.get_one(user_id)
            data["id"] = user_id
            UserSchema().dump(user_service.update_password(data, user))
            return "", HTTPStatus.NO_CONTENT

        if not data:
            raise HTTPStatus.BAD_REQUEST

        if not data.get("old_password") or not data.get("new_password"):
            raise HTTPStatus.BAD_REQUEST
