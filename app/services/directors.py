from app.dao.director import DirectorDAO


class DirectorsService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did):
        return self.dao.get_one(did)
