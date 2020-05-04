from tweetlib import tweet_image
from tweetlib import tweet
from tweetlib import getTweets
import json


r = open('status.txt', 'r')
s = r.read()
r.close()
w = open('status.txt', 'w')
#if s == "1":
#   w.write('0')
#   message = "Hey, it's xander"
#   tweet_image('https://i.imgflip.com/2qihoc.jpg', message)
#else:
#    w.write('1')
#    message = "Maybe I'm pivoting."
#    url = 'https://i.imgflip.com/2qihoc.jpg'
#    tweet_image(url, message)
if s == "1":
    w.write('2')
    message = "Sir, this is a Wendy's."
elif s == "2":
    w.write('3')
    message = "Sir, this is an Arby's."
else:
    w.write("1")
    message = "Sir, this is the breadline."
#respond to tweet with one of these messages.
son = getTweets("agadmator")

msg = son[0]
print(msg.favorite_count)
json_str = json.dumps(msg._json)

parsed = json.loads(json_str)
print(json.dumps(parsed, indent=4, sort_keys = True))

