import tweepy
import requests
import os
from tweetlib import twitter_api
api = twitter_api()
def contains(text, words):
    wrd = len(words)
    r = False
    while(not r and wrd > 0):
        r = words[wrd - 1] in text
        wrd = wrd - 1
    return r
def tweet_image(url, message):
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

def sir(text):
    for c in text:
        if not(c.isupper()) and c.isalpha():
            print("Sir, this is a Wendy's.")
            return
    print("Sir, this is an Arby's.");

words = ['hello', 'stuff']
text = "Hello, this is stuff"

url = 'https://pbs.twimg.com/media/D1Je_eSXQAEIyRV.jpg'
message = '#NewProfilePic'
tweet_image(url, messagv)
