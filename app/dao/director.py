from sqlalchemy.orm import scoped_session

from app.dao.models.director import Director
from app.exceptions import DirectorNotFound


class DirectorDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def get_all(self):
        entity_list = self.session.query(Director).all()
        try:
            return entity_list
        except NameError:
            raise DirectorNotFound

    def get_one(self, pk):
        entity_list = self.session.query(Director).filter(Director.id == pk).one_or_none()
        try:
            return entity_list
        except NameError:
            raise DirectorNotFound
