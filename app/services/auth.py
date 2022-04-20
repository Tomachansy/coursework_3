import calendar
import datetime
import jwt
from flask import request

from app.config import BaseConfig
from app.exceptions import InvalidCredentials, InvalidTokens
from app.services.users import UsersService


class AuthService:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise InvalidCredentials

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise InvalidTokens
        data = {
            "email": user.email
        }

        # minutes for access_token
        min_ = datetime.datetime.utcnow() + datetime.timedelta(minutes=BaseConfig.TOKEN_EXPIRE_MINUTES)
        data["exp"] = calendar.timegm(min_.timetuple())
        access_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.JWT_ALGORITHM)

        # days for refresh_token
        days_ = datetime.datetime.utcnow() + datetime.timedelta(days=BaseConfig.TOKEN_EXPIRE_DAYS)
        data["exp"] = calendar.timegm(days_.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.JWT_ALGORITHM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.JWT_ALGORITHM])
        email = data.get('email')
        user = self.user_service.get_by_email(email)
        if user is None:
            raise InvalidCredentials

        return self.generate_tokens(email, user.password, is_refresh=True)
