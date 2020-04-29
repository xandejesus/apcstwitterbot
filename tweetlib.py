# just use this file to get the accesstokens and api.
import tweepy
def twitter_api():
    tokenfile = '../accesstokens'
    with open(tokenfile) as f:
        r = f.read()
        ak, ask, at, ats = r.split()
    auth = tweepy.OAuthHandler(ak, ask)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth)
    return api

