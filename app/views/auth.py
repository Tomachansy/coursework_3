from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource

from app.implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthView(Resource):
    @auth_ns.response(int(HTTPStatus.CREATED), 'User registration success')
    @auth_ns.response(int(HTTPStatus.CONFLICT), 'User already exists')
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), 'Invalid json message received')
    def post(self):
        """Register a new user"""
        data = request.json

        if not data:
            raise HTTPStatus.BAD_REQUEST
        user_service.create(data)
        return HTTPStatus.CREATED


@auth_ns.route('/login/')
class AuthView(Resource):
    @auth_ns.response(int(HTTPStatus.OK), 'OK')
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), 'Email and/or password are incorrect')
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), 'Invalid json message received')
    def post(self):
        """User authorization and tokens generation"""
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            raise HTTPStatus.BAD_REQUEST
        tokens = auth_service.generate_tokens(email, password)
        return tokens, HTTPStatus.OK

    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), 'Token is invalid or expired')
    def put(self):
        """Approve refresh token and get access"""
        data = request.json

        token = data.get("refresh_token")

        if not data:
            raise HTTPStatus.BAD_REQUEST
        try:
            tokens = auth_service.approve_refresh_token(token)
            return tokens, HTTPStatus.OK
        except NameError:
            raise HTTPStatus.UNAUTHORIZED
