from flask import render_template
from . import main


@main.route("/")
def unwind():
    app_name = "UNWINDING"

    return render_template("unwind.html", app_name=app_name)

