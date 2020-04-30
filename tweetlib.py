# just use this file to get the accesstokens and api.
import tweepy
import requests
import os


def twitter_api():
    tokenfile = '../accesstokens'
    with open(tokenfile) as f:
        r = f.read()
        ak, ask, at, ats = r.split()
    auth = tweepy.OAuthHandler(ak, ask)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth)
    return api

# idk, gets tweets
def getTweets(user):
    api = twitter_api()
    tweets = api.user_timeline(screen_name=user)
    first_tweet = tweets[0]
    print(first_tweet.text)
    return tweets
# Duplicate of sendtweet.py, just making things accessible in one file.

def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download Image")
def tweet(message):
    api = twitter_api()
    api.update_status(message)

