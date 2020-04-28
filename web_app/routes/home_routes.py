
# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def hello_world():
    print("YOU VISITED THE HOMEPAGE")
    #return "Hello, World!"
    return render_template("prediction_form.html")

@home_routes.route("/about")
def about():
    print("YOU VISITED THE ABOUT PAGE")
    return "About Me (TODO)"
