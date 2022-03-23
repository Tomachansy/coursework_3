from marshmallow import Schema, fields

from app.dao.models.genre import GenreSchema
from app.setup_db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String, nullable=True)
    favourite_genre = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=True)
    favourites = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    name = fields.Str(required=False)
    surname = fields.Str(required=False)
    favourite_genre = fields.Int(required=False)
    favourites = fields.Nested(GenreSchema, dump_only=True)
