import tweepy
from datetime import datetime,timezone
import pytz
import pandas as pd
import message
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

api_key        = os.getenv('API_KEY')
api_key_secret     = os.getenv('API_KEY_SECRET')
access_token        = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token      = os.getenv('BEARER_TOKEN')
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token
)

# 最新のツイートを取得
tweets = client.search_recent_tweets(query='from:ngnchiikawa',  # 検索ワード
                                     max_results=10  # 取得件数
                                    )
newTweet=(tweets[0][0].text)
f = open('myfile.txt', 'r', encoding='UTF-8') 
data=f.read()
print(data)
print(newTweet)
if data != newTweet and 'https' in newTweet and 'RT' not in newTweet:
    message.send_message(newTweet)
    f = open('myfile.txt', 'w', encoding='UTF-8') 
    f.write(newTweet)
    f.close()
