import tweepy
from secrets import BEARER_TOKEN



def get_tweets():
    client = tweepy.Client(BEARER_TOKEN)
    response = client.search_recent_tweets("Tweepy")
    tweets = response.data
    print(tweets)



