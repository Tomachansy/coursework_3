import jwt
from flask import request, abort

from app.config import BaseConfig
from app.implemented import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            user_data = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.JWT_ALGORITHM])
            user = user_service.get_by_email(user_data["email"])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs, user_id=user.id)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        role = None

        try:
            user = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.JWT_ALGORITHM])
            role = user.get("role", "user")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
