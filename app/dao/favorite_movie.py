from sqlalchemy import desc
from sqlalchemy.orm import scoped_session

from app.dao.models import FavoriteMovie
from app.exceptions import FMovieAlreadyExists


class FavoriteMovieDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def get_all_by_id(self, user_id):
        entity_list = self.session.query(FavoriteMovie).filter(FavoriteMovie.user_id == user_id).all()
        return entity_list

    def get_filter(self, limit, offset, status, user_id):
        if limit > 0 and status == "new":
            return self.session.query(FavoriteMovie).filter(FavoriteMovie.user_id == user_id).\
                order_by(desc(FavoriteMovie.year)).limit(limit).offset(offset).all()
        if limit > 0:
            return self.session.query(FavoriteMovie).filter(FavoriteMovie.user_id == user_id).\
                limit(limit).offset(offset).all()
        if status == "new":
            return self.session.query(FavoriteMovie).filter(FavoriteMovie.user_id == user_id).\
                order_by(desc(FavoriteMovie.year)).all()

    def create(self, user_id, movie_id):
        movie = self.session.query(FavoriteMovie).filter(FavoriteMovie.movie_id == movie_id).first()
        if not movie:
            entity = FavoriteMovie(user_id=user_id, movie_id=movie_id)
            self.session.add(entity)
            self.session.commit()

            return entity
        else:
            raise FMovieAlreadyExists

    def delete(self, user_id, movie_id):
        entity = self.session.query(FavoriteMovie).filter(
            FavoriteMovie.user_id == user_id,
            FavoriteMovie.movie_id == movie_id
        ).one_or_none()

        self.session.delete(entity)
        self.session.commit()

        return entity
