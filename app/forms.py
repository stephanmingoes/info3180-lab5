from wtforms import Form, TextAreaField,FileField, StringField, PasswordField, validators
from werkzeug.utils import secure_filename

def validate_image(form, field):
    if field.data:
        filename = secure_filename(field.data.filename)
        if not filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            raise validators.ValidationError('Invalid file format. Please upload an image.')

class MovieForm(Form):
    title = StringField('title', [validators.DataRequired()])
    description = TextAreaField('description', validators=[
        validators.DataRequired(),
        validators.Length(min=10, max=1000)
    ])
    poster = FileField('poster', validators=[
        validators.DataRequired(),
        validate_image
    ])
