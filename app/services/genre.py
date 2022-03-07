from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        genre = self.get_one(data.get("id"))
        genre.name = data.get("name")

        self.dao.update(genre)

    def update_partial(self, data):
        genre = self.get_one(data.get("id"))

        if "name" in data:
            genre.name = data.get("name")

        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)
