from app.dao import FavoriteMovieDAO
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.user import UserDAO
from app.services.directors import DirectorsService
from app.services.favorite_movies import FavoriteMoviesService
from app.services.genres import GenresService
from app.services.movies import MoviesService
from app.services.users import UsersService
from app.services.auth import AuthService
from app.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
fav_movie_dao = FavoriteMovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)


director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
fav_movie_service = FavoriteMoviesService(dao=fav_movie_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
