from sqlalchemy.orm import scoped_session

from app.dao.models.user import User
from app.exceptions import UserAlreadyExists, UserInfoUpdateError, PasswordUpdateError


class UserDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(User).filter(User.id == pk).one_or_none()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one_or_none()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        entity = User(**user_data)
        user_email = user_data.get("email")
        user = self.get_by_email(user_email)

        if not user:
            self.session.add(entity)
            self.session.commit()

            return entity
        else:
            raise UserAlreadyExists

    def update_user(self, user_data):
        uid = user_data.get("id")
        user = self.get_one(uid)
        user.name = user_data.get("name")
        user.surname = user_data.get("surname")
        user.favourite_genre = user_data.get("favourite_genre")

        try:
            self.session.add(user)
            self.session.commit()
        except NameError:
            raise UserInfoUpdateError
        return user

    def update_password(self, user_data):
        uid = user_data.get("id")
        user = self.get_one(uid)
        user.password = user_data.get("password")

        try:
            self.session.add(user)
            self.session.commit()
        except NameError:
            raise PasswordUpdateError
        return user
