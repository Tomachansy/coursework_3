from .auth import auth_ns
from .director import directors_ns
from .favorite_movie import favorite_movies_ns
from .genre import genres_ns
from .movie import movies_ns
from .user import users_ns

__all__ = [
    "genres_ns",
    "directors_ns",
    "movies_ns",
    "favorite_movies_ns",
    "users_ns",
    "auth_ns"
]
