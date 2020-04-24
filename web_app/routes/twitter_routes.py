# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify #, render_template, request, flash, redirect

from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api
from web_app.services.basilica_service import connection as basilica_connection

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    print("FETCHING...", screen_name)

    #
    # fetch user info
    #
    user = twitter_api.get_user(screen_name)

    #
    # store user info in database
    #

    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()

    #
    # fetch their tweets
    #

    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=150)
    print("STATUSES", len(statuses))

    #
    # fetch embedding for each tweet
    #

    tweet_texts = [status.full_text for status in statuses]
    embeddings = list(basilica_connection.embed_sentences(tweet_texts, model="twitter"))
    print("EMBEDDINGS", len(embeddings))

    #
    # store tweets in database (w/ embeddings)
    #

    for index, status in enumerate(statuses):
        print(status.full_text)
        print("----")
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id
        db_tweet.full_text = status.full_text
        embedding = embeddings[index]
        print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)

    db.session.commit()

    return f"FETCHED {screen_name} OK"
    #return jsonify({"user": user._json, "num_tweets": len(statuses)})
