from sqlalchemy.orm import scoped_session

from app.dao.models.genre import Genre
from app.exceptions import GenreNotFound


class GenreDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def get_all(self):
        entity_list = self.session.query(Genre).all()
        try:
            return entity_list
        except NameError:
            raise GenreNotFound

    def get_one(self, pk):
        entity_list = self.session.query(Genre).filter(Genre.id == pk).one_or_none()
        try:
            return entity_list
        except NameError:
            raise GenreNotFound
