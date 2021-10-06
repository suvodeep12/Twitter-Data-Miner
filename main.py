import sys

import tweepy

consumer_key = "<consumer key>"
consumer_secret = "<consumer key secret>"
access_token = "<access token>"
access_token_secret = "<access token secret>"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)


def timeline():
    # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
    public_tweets = api.home_timeline()
    # foreach through all tweets pulled
    for tweet in public_tweets:
        # printing the text stored inside the tweet object
        print(tweet.text)
        # printing the username of the tweeter
        print(tweet.user.screen_name)
        # printing the location of the tweeter
        print(tweet.user.location)


def user(name):
    # Number of tweets to pull
    tweetcount = 20

    # Calling the user_timeline function with our parameters
    results = api.user_timeline(id=name, count=tweetcount)

    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.text)


def keyword(query):
    language = "en"

    # Calling the user_timeline function with our parameters
    results = api.search(q=query, lang=language)

    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.user.screen_name, "Tweeted:", tweet.text)


print("1.\tShow tweets from timeline\n2.\tShow tweets from user\n3.\tShow tweets by keyword\n\n0.\tExit")
choice = input()
# Trying Python 3.10 match case
match choice:
    case 0:
        sys.exit()
    case 1:
        timeline()
    case 2:
        print("Enter userid without '@'")
        main_user = input()
        user(main_user)
    case 3:
        print("Enter keyword without '#'")
        main_keyword = input()
        keyword(main_keyword)
    case _:
        print("Invalid response!")
