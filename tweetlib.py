# just use this file to get the accesstokens and api.
import tweepy
import requests
import os
import re
from nltk.tokenize import WordPunctTokenizer
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def twitter_api():
    tokenfile = '../accesstokens'
    with open(tokenfile) as f:
        r = f.read()
        ak, ask, at, ats = r.split()
    auth = tweepy.OAuthHandler(ak, ask)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth)
    return api

def getSince(user):
    s = user + ".txt"
    r = open(s, 'r')
    lasttweet = r.read()
    r.close()
    return r
def addSince(user, idnum):
    s = user + ".txt"
    w = open(s, 'w')
    w.write(idnum)
    


# From freeCodeCamp

def cleantweet(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet)
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]',' ',link_removed)
    lower_case_tweet = number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    return clean_tweet

def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types\
            .Document(content=tweet, 
                    type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                    .analyze_sentiment(document = document)\
                    .document_sentiment\
                    .score
    return sentiment_score


# Easy for the bot to be able to send tweets from a twitter bot. IDK
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

