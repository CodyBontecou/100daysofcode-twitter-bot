import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

from StreamListener import StreamListener

auth = tweepy.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets_listener = StreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener, tweet_mode="extended", snooze_time_step=720000)
stream.filter(track=["100DaysOfCode", "DEVCommunity"], languages=["en"])
