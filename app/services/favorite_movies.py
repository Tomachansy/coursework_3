from app.config import BaseConfig
from app.dao.favorite_movie import FavoriteMovieDAO


class FavoriteMoviesService:
    def __init__(self, dao: FavoriteMovieDAO):
        self.dao = dao

    def get_by_user_id(self, user_id):
        return self.dao.get_all_by_id(user_id)

    def get_filter_fav_movies(self, filters, user_id):
        limit = 0
        offset = 0
        if filters.get("page"):
            limit = BaseConfig.ITEMS_PER_PAGE
            offset = (filters.get("page") - 1) * limit
        status = filters.get("status")
        return self.dao.get_filter(limit=limit, offset=offset, status=status, user_id=user_id)

    def create(self, user_id, movie_id):
        return self.dao.create(user_id, movie_id)

    def delete(self, user_id, movie_id):
        return self.dao.delete(user_id, movie_id)
