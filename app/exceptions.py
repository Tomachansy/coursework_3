from http import HTTPStatus
from typing import Dict


class BaseHTTPResponse(Exception):
    description: str = "Server error"
    code: int = HTTPStatus.INTERNAL_SERVER_ERROR

    def message(self) -> Dict[str, str]:
        return {"message": self.description}


class ItemNotFound(BaseHTTPResponse):
    code = HTTPStatus.NOT_FOUND


class MovieNotFound(ItemNotFound):
    description = "Movie not found"


class DirectorNotFound(ItemNotFound):
    description = "Director not found"


class GenreNotFound(ItemNotFound):
    description = "Genre not found"


class ItemAlreadyExists(BaseHTTPResponse):
    code = HTTPStatus.CONFLICT


class UserAlreadyExists(ItemAlreadyExists):
    description = "User with this email already exists"


class FMovieAlreadyExists(ItemAlreadyExists):
    description = "This movie already exists in favorites"


class InvalidAuthorization(BaseHTTPResponse):
    code = HTTPStatus.UNAUTHORIZED


class InvalidCredentials(InvalidAuthorization):
    description = "Email and/or password are incorrect"


class InvalidTokens(InvalidAuthorization):
    description = "Token is invalid or expired"


class UpdateError(BaseHTTPResponse):
    code = HTTPStatus.BAD_REQUEST


class UserInfoUpdateError(UpdateError):
    description = "Change user information failed"


class PasswordUpdateError(UpdateError):
    description = "Change password failed"
