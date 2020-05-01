# The driver code for the bot. Doesn't look like much, but the bot wouldn't be able to run without it.
# These are two simple functions that do what they look like they do
#todo: make a scraper that gets King Mango's tweets(not that hard)
# sort the tweets by priority of least to most crazy, likely factoring in likes and comments

import tweepy
from tweetlib import twitter_api
def contains(text, words):
    wrd = len(words)
    r = False
    while(not r and wrd > 0):
        r = words[wrd - 1] in text
        wrd = wrd - 1
    return r

def sir(text):
    for c in text:
        if not(c.isupper()) and c.isalpha():
            print("Sir, this is a Wendy's.")
            return
    print("Sir, this is an Arby's.");

words = ['hello', 'stuff']
text = "Hello, this is stuff"

