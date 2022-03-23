import base64
import hashlib
import hmac

from app.config import BaseConfig
from app.dao.user import UserDAO
from app.exceptions import PasswordUpdateError


class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, user_data):
        user_data["password"] = self.get_hash(user_data["password"])
        return self.dao.create(user_data)

    def update_user(self, user_data, user_id):
        if "name" in user_data:
            user_id.name = user_data.get("name")
        if "surname" in user_data:
            user_id.surname = user_data.get("surname")
        if "favourite_genre" in user_data:
            user_id.favourite_genre = user_data.get("favourite_genre")

        return self.dao.update_user(user_data)

    def update_password(self, user_data, user_id):
        user_password = user_id.password
        password_1 = user_data["old_password"]
        password_2 = user_data["new_password"]

        if self.compare_passwords(user_password, password_1):
            user_data["password"] = self.get_hash(password_2)
            return self.dao.update_password(user_data)
        else:
            raise PasswordUpdateError

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)

