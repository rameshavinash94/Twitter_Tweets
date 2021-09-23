#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------------------
# Twitter service that implement any Twitter API to programmatically
# create, retrieve and delete a Tweet using Twitter APIs
# Authors: charu.cheema@sjsu.edu, poojashree.ns@sjsu.edu, avinash.ramesh@sjsu.edu , nishamohan.devadiga@sjsu.edu
# -------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, request, redirect, url_for
import tweepy
import re

app = Flask(__name__)
app.config.from_object('config')

# Default landing page

@app.route('/')
def default_redirect():
    return redirect(url_for('tweets'))

# This method fetches tweets for specified user
@app.route('/tweets', methods=['GET'])
def tweets():
    public_tweets = api.user_timeline(app.config["TWITTER_APP_USER_ID"])
    return render_template('tweets.html', tweets=public_tweets)

# Author: poojashree.ns@sjsu.edu
# This method fetches tweets for specified user and as per keyword provided
@app.route('/tweets/search', methods=['POST'])
def fetch_tweets():
    tweet_view = []
    key_tweets = ''
    key_tweet = request.form['key_tweet']
    public_tweets = api.user_timeline()
    for all_tweets in tweepy.Cursor(api.user_timeline).items():
        regex = re.findall('.*' + key_tweet + '.*', all_tweets.text)
        if len(regex) == 1:
            key_tweets = api.get_status(str(all_tweets.id))
            tweet_view.append(key_tweets)
    return render_template('tweets.html', tweets_view=tweet_view,
                           tweets=public_tweets)

 #Author: avinash.ramesh@SJSU.edu
# This method deletes a tweet based on provided tweet Id and the Recent activity in tweets.html gets updated accordingly.
@app.route('/tweet/delete', methods=['POST'])
def delete_tweet():
    to_be_deleted = request.form['to_be_deleted']
    api.destroy_status(to_be_deleted)
    return redirect(url_for('tweets'))


# Author: nishamohan.devadiga@sjsu.edu
# This method posts a new tweet

@app.route('/tweets', methods=['POST'])
def post_tweet():
    new_tweet = request.form['new_tweet']
    api.update_status(new_tweet)
    return redirect(url_for('tweets'))


# Main method handles authentication based of keys and secrets in config.py
# Author: charu.cheema@sjsu.edu

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(app.config['TWITTER_CONSUMER_KEY'],
                               app.config['TWITTER_CONSUMER_SECRET'])
    auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'],
                          app.config['TWITTER_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print ('Authentication successful')
    except:
        print ('Authentication Error')

    app.run(debug=True)