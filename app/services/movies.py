from app.config import BaseConfig
from app.dao.movie import MovieDAO


class MoviesService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_filter_movies(self, filters):
        limit = 0
        offset = 0
        if filters.get("page"):
            limit = BaseConfig.ITEMS_PER_PAGE
            offset = (filters.get("page") - 1) * limit
        status = filters.get("status")
        return self.dao.get_filter(limit=limit, offset=offset, status=status)
