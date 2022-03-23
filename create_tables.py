from app.config import DevelopmentConfig
from app.dao.models import *  # noqa F401, F403
from app.server import create_app
from app.setup_db import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
