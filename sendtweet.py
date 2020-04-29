import tweepy
import requests
import os
from tweetlib import twitter_api
api = twitter_api()
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
url = 'https://www.shutupandtakemymoney.com/wp-content/uploads/2020/04/kim-jong-un-coffin-guys-friend-request-meme.jpg'
message = 'unfortunately cannot tweet gifs. rip'
tweet_image(url,message)
