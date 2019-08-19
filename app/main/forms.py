from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    ValidationError,
    SelectField,
    IntegerField,
)
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class AddPomodoroForm(FlaskForm):
    submit = SubmitField("Add Pomodoro")


class SignInForm(FlaskForm):
    submit = SubmitField("Sign in")


class SettingsForm(FlaskForm):
    duration = IntegerField("Pomodoro duration", validators=[Required()])
    short_break = IntegerField("Break duration", validators=[Required()])
    date_format = SelectField(
        "Date Format",
        choices=[
            ("MM/DD/YY", "MM/DD/YY"),
            ("MM-DD-YY", "MM-DD-YY"),
            ("YYY-MM-DD", "YYY-MM-DD"),
            ("YYY.MM.DD", "YYY.MM.DD"),
        ],
    )
    time_format = SelectField(
        "Time Format", choices=[("%H:%M:%S", "24 Hour"), ("%I:%M %p", "12 Hour")]
    )
    submit = SubmitField("Save")
