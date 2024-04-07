from flask import Flask
from .config import Config
from flask_migrate import Migrate
from app.db import db
from app.models import Movie


app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])

db.init_app(app)
migrate = Migrate(app, db)

from app import views

