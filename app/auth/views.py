from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            flash("Logged in")
            login_user(user)
            print(user)
            return redirect(url_for("main.unwind"))
        else:
            flash("Invalid username or Password")
            return render_template("auth/login.html", form=form)

    flash("All fields are required")
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Successfully registered!")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
