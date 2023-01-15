# import the module
import os
import tweepy
import psycopg2
from pytz import timezone
from datetime import datetime

ACCESS_KEY = os.environ["ACCESS_KEY"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]

HOST_NAME = os.environ["HOST_NAME"]
DATABASE = os.environ["DATABASE"]
USER = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]


auth = tweepy.OAuthHandler(ACCESS_KEY, ACCESS_SECRET)
auth.set_access_token(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

woeid_india = 2282863
woeid_us = 2357024
woeid_world = 1

trends_india = api.get_place_trends(id = woeid_india)
trends_us = api.get_place_trends(id = woeid_us)
trends_worldwide = api.get_place_trends(id = woeid_world)

current_time = datetime.now().replace(microsecond=0, second=0, minute=0)
local_tz = timezone("Asia/Calcutta")
current_time = local_tz.localize(current_time)

conn = psycopg2.connect(
    host=HOST_NAME,
    database=DATABASE,
    user=USER,
    password=PASSWORD)


# Create a cursor
cur = conn.cursor()

for i in range(3):
    if i == 0:
        trends = trends_india
        region = 'India'
    if i == 1:
        trends = trends_us
        region = 'USA'
    if i == 2:
        trends = trends_worldwide
        region = 'Worldwide'
    for value in trends:
        for trend in value['trends']:
            record = (current_time, region, trend['name'], trend['tweet_volume'])
            query = "INSERT INTO twitter_trends VALUES (%s, %s, %s, %s)"
            cur.execute(query, record)
            conn.commit()


cur.close()
conn.close()
