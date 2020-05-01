import tweepy
from tweetlib import twitter_api
api = twitter_api()
tweets = api.user_timeline(screen_name="realDonaldTrump")
n = 0
for tweet in tweets:
    n += 1
    print(str(n) + " " + tweet.text)
