from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from flask import Blueprint, jsonify, request, flash, redirect # render_template

from web_app.statsmodels import load_model

stats_routes = Blueprint("stats_routes", __name__)

# TODO: accept some inputs related to the iris training data (x values)
@stats_routes.route("/stats/iris")
def iris():
    X, y = load_iris(return_X_y=True)
    clf = load_model() # make sure to pre-train the model first!
    result = str(clf.predict(X[:2, :]))
    print("PREDICTION", result)
    return result # todo: return as JSON

# TODO: accept some inputs related to the iris training data (x values)
@stats_routes.route("/stats/predict", methods=["POST"])
def twitoff_predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form)) #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]
    print(screen_name_a, screen_name_b, tweet_text)

    # TODO: train a model

    # TODO: make a prediction and return it

    return "OK (TODO)"
