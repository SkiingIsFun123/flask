from flask import Blueprint
from flask import render_template

frontend = Blueprint("frontend", __name__, template_folder="templates")

# Returns "index.html" from the frontend folder when "/" accessed by the user
@frontend.route("/")
def index():
    return render_template("frontend/index.html")


# Returns "missing_template.html" when "/missing" is accessed by the user
@frontend.route("/missing")
def missing_template():
    return render_template("missing_template.html")
