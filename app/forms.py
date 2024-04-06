from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length

images = UploadSet('images', IMAGES)
class MovieForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[
        DataRequired(),
        Length(min=10, max=1000)
    ])
    poster = FileField('poster', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
