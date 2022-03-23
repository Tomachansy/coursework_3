from sqlalchemy.exc import IntegrityError

from app.config import DevelopmentConfig
from app.dao.models import Genre, Movie, Director
from app.server import create_app
from app.setup_db import db
from app.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")

    for director in data["directors"]:
        db.session.add(Director(id=director["pk"], name=director["name"]))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")

    for movie in data["movies"]:
        db.session.add(Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"]
        ))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
