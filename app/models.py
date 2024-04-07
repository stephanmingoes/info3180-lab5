from app import db
from datetime import datetime

class Movie(db.Model):
    """
    This class represents a movie in the database.
    """
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, new_movie):
        self.title = new_movie['title']
        self.description = new_movie['description']
        self.poster = new_movie['poster']

    def __repr__(self):
        return f'<Movie {self.id} - {self.title}>'
