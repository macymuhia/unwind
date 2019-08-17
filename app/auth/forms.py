from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Required()])
    email = StringField("Email", validators=[Required(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            Required(),
            EqualTo("confirm_password", message="Passwords must match"),
        ],
    )
    confirm_password = PasswordField("Confirm Password", validators=[Required()])
    submit = SubmitField("Sign Up")

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("That username is taken")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    submit = SubmitField("Sign In")
