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

print(ACCESS_KEY)
print(ACCESS_SECRET)
print(CONSUMER_KEY)
print(CONSUMER_SECRET)
