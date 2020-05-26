from tweetlib import *
import random
import tweepy

def clean(stuff):
    for i in range(len(stuff)):
        c = stuff[i]
        c = c[:-2]
        stuff[i] = c

def getwords():
    r = open('words.txt', 'r')
    words = r.readlines()
    return words

def getscore(tweet):
    clean = cleantweet(tweet.text)
    score = gets_sentiment_score(clean)
    try:
        likes = tweet.retweeted_status.favorite_count
    except:
        likes = tweet.favorite_count
    return score * -100000 + likes

def addtweets(tweets, sentiments):
    api = twitter_api()
    try:
        with open('tweet.txt', 'r') as r:
            tweetlist = r.readlines()
    except:
        return tweets, sentiments
    with open('sentiments.txt', 'r') as r:
        sentimentlist = r.readlines()
    clean(sentimentlist)
    print(tweetlist)
    for j in range(len(tweetlist)):
        tweet = api.get_status(tweetlist[j])
        t1 = tweet.favorite_count + -10000 * float(sentimentlist[j])
        for i in range(len(tweets)):
            t2 = tweets[i].favorite_count + float(sentiments[i]) * -10000
            if(not(t2 > t1)):
                tweets.append(tweets[len(tweets)-1])
                sentiments.append(sentiments[len(sentiments)-1])
                for k in range(len(tweets) - 1, i, -1):
                    tweets[k] = tweets[k-1]
                    sentiments[k] = sentiments[k-1]
                tweets[i] = tweet
                sentiments[i] = sentimentlist[j]
                break
            if(i == len(tweets) - 1):
                tweets.append(tweet)
                sentiments.append(sentimentlist[j])
    return tweets, sentiments

def getmessage():
    with open('tweetmessages.txt', 'r') as r:
        messages = r.readlines()
    for message in messages:
        message = message[:-2]
    return messages

def tweetmessage(tweet, user):
    
    api = twitter_api()
    messages = getmessage()
    message = messages[random.randrange(len(messages))]
    message = "@" + user + " " + message
    api.update_status(message, tweet.id)

def getvictim():
    try:
        with open('api.txt', 'r') as r:
            user = r.readline()
    except:
        user = "realDonaldTrump"
    return user

def main():
    tweetlist = []
    sentiments = []
    api = twitter_api()
    user = getvictim()
    try:
        with open('tweetdata.txt', 'r') as r:
            old = r.readline()
        tweets = api.user_timeline(screen_name=user, count=12, max_id=old)
    except:
        tweets = api.user_timeline(screen_name=user, count=12)
    with open('tweetdata.txt', 'w') as w:
        w.write(str(tweets[len(tweets) - 1].id))
    for tweet in tweets:
        print(tweet.text)
        text = cleantweet(tweet.text)
        sentiment = get_sentiment_score(text)
        if sentiment < -.6:
            sentiments.append(sentiment)
            tweetlist.append(tweet)
    for i in range(len(tweetlist)):
        n = len(tweetlist)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                t1, t2 = tweetlist[j], tweetlist[j+1]
                s1, s2 = sentiments[j], sentiments[j+1]
                try:
                    t2f = t2.retweeted_status.favorite_count
                except:
                    t2f = t2.favorite_count
                try:
                    t1f = t1.retweeted_status.favorite_count
                except:
                    t1f = t1.favorite_count
                p1 = s1 * -100000 + t1f
                p2 = s2 * -100000 + t2f
                if p1 < p2:
                    tweetlist[j], tweetlist[j+1]  = t2, t1
                    sentiments[j], sentiments[j+1] = s2, s1
    

    for i in range(0, len(tweetlist)):
        tweet = tweetlist[i].text
        print("Tweet: {}".format(cleantweet(tweet)))
        print("Sentiment: {}\n".format(str(sentiments[i])))
        try:
            t = tweetlist[i].retweeted_status.favorite_count
        except:
            t = tweetlist[i].favorite_count
        print("Likes: {}".format(t))
        print("Total Score:{}".format(t + sentiments[i] * -100000))    
    tweetlist, sentiments = addtweets(tweetlist, sentiments) 
    tweetlist1 = []
    sentiments1 = []
    for i in range(6):
        tweetlist1.append(tweetlist[i])
        sentiments1.append(sentiments[i])
    with open('tweet.txt','w') as w:
        for tweet in tweetlist1:
            w.write(str(tweet.id) + "\n")
    with open('sentiments.txt', 'w') as w:
        for sentiment in sentiments1:
            w.write(str(sentiment) + "\n")

    tweetmessage(tweetlist1[0], user)

main()
