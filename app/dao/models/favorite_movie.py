from marshmallow import Schema, fields

from app.dao.models.movie import MovieSchema
from app.dao.models.user import UserSchema
from app.setup_db import db


class FavoriteMovie(db.Model):
    __tablename__ = 'favorite_movies'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    movie = db.relationship("Movie")


class FavoriteMovieSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    user = fields.Nested(UserSchema, dump_only=True)
    movie_id = fields.Int()
    movie = fields.Nested(MovieSchema, dump_only=True)
