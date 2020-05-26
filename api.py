from tweetlib import *
import tweepy
api = twitter_api()
snek = False
while True:
    twitter_handle = input("Enter twitter handle (eg Shadbase): ")
    try:
        u = api.get_user(screen_name=twitter_handle)
        break
    except:
        print("User doesn't exist")
with open("data/api.txt", 'w') as w:
    w.write(twitter_handle)
