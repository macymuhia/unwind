from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from . import main
from .forms import SignInForm
from ..models import User
from .. import db


@main.route("/", methods=["GET", "POST"])
def index():
    app_name = "Welcome HOME"
    form = SignInForm()

    if form.validate_on_submit():
        return redirect(url_for("auth.login"))

    return render_template("index.html", app_name=app_name, form=form)


@main.route("/unwind")
@login_required
def unwind():
    app_name = "UNWINDING"

    return render_template("unwind.html", app_name=app_name)
