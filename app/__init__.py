from flask import Flask
from .config import Config
from flask_migrate import Migrate
from app.db import db
from app.models import Movie
from flask_wtf.csrf import CSRFProtect 


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])

db.init_app(app)
migrate = Migrate(app, db)

from app import views

