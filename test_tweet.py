from tweetlib import tweet_image
from tweetlib import tweet
r = open('status.txt', 'r')
s = r.read()
r.close()
w = open('status.txt', 'w')
if s == "1":
   w.write('0')
   message = "Hey, it's xander"
   tweet_image('https://i.imgflip.com/2qihoc.jpg', message)
else:
    w.write('1')
    message = "Maybe I'm pivoting."
    url = 'https://i.imgflip.com/2qihoc.jpg'
    tweet_image(url, message)
w.close()
