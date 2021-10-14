import tweepy
import json


class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        try:
            text = tweet.extended_tweet["full_text"]
        except AttributeError:
            text = tweet.text
        if len(text.split("#")) < 3 and text.split(' ')[0] != 'RT':
            print(f"{text}")
            self.api.create_favorite(tweet.id)

    def on_error(self, status):
        print("Error detected")