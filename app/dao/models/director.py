from marshmallow import Schema, fields
from app.setup_db import db


class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    name = fields.Str(required=True)

