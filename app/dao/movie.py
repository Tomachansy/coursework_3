from sqlalchemy import desc
from sqlalchemy.orm import scoped_session

from app.dao.models.movie import Movie
from app.exceptions import MovieNotFound


class MovieDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def get_all(self):
        entity_list = self.session.query(Movie).all()
        try:
            return entity_list
        except NameError:
            raise MovieNotFound

    def get_one(self, pk):
        entity_list = self.session.query(Movie).filter(Movie.id == pk).one_or_none()
        try:
            return entity_list
        except NameError:
            raise MovieNotFound

    def get_filter(self, limit, offset, status):
        if limit > 0 and status == "new":
            return self.session.query(Movie).order_by(desc(Movie.year)).limit(limit).offset(offset).all()
        if limit > 0:
            return self.session.query(Movie).limit(limit).offset(offset).all()
        if status == "new":
            return self.session.query(Movie).order_by(desc(Movie.year)).all()
        raise MovieNotFound
