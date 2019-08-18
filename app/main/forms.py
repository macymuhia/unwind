from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class SignInForm(FlaskForm):
    submit = SubmitField("Sign in")
