from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from werkzeug.routing import ValidationError
from config import Config

class EntryForm(FlaskForm):
    title = StringField('Text', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    is_published = BooleanField('Is_Published', default="checked")


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, field):
        if field.data != Config.ADMIN_USERNAME:
            raise ValidationError("Invalid username")
        return field.data

    def validate_password(self, field):
        if field.data != Config.ADMIN_PASSWORD:
            raise ValidationError("Invalid password")
        return field.data