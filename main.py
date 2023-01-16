# This code imports the necessary libraries for connecting to a 
# PostgresSQL database, accessing the Twitter API, 
# and working with timezones and datetimes.
import os
import tweepy
import psycopg2
from pytz import timezone
from datetime import datetime

# Retrieve environment variables for keys and secrets
# to access the Twitter API
ACCESS_KEY = os.environ["ACCESS_KEY"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]

# Retrieve environment variables for connecting to the database
# HOST_NAME, DATABASE, USER, and PASSWORD
HOST_NAME = os.environ["HOST_NAME"]
DATABASE = os.environ["DATABASE"]
USER = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]

# Setting up the authentication using tweepy and the necessary keys to access the API.
auth = tweepy.OAuthHandler(ACCESS_KEY, ACCESS_SECRET)
auth.set_access_token(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

# Assigns each WOEID (Where On Earth ID) to a different location; 
# India, the US, and the world respectively.
woeid_india = 2282863
woeid_us = 2357024
woeid_world = 1

# This code retrieves the trending topics from India, the US, and worldwide, 
# using the corresponding woeid (Where on Earth Identifier) for each area.
trends_india = api.get_place_trends(id = woeid_india)
trends_us = api.get_place_trends(id = woeid_us)
trends_worldwide = api.get_place_trends(id = woeid_world)

# This code sets the current time to the start of the current hour in the Asia/Calcutta timezone.
current_time = datetime.now().replace(microsecond=0, second=0, minute=0)
local_tz = timezone("Asia/Calcutta")
current_time = local_tz.localize(current_time)

# Establishing a connection to the PostgreSQL database using the connection parameters provided.
conn = psycopg2.connect(
    host=HOST_NAME,
    database=DATABASE,
    user=USER,
    password=PASSWORD)

# Create a cursor to interact with the database connection
cur = conn.cursor()

# This code creates a cursor and loops through 3 different regions (India, USA, Worldwide) 
# to extract trend information from each region and insert them into the database.
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

# Closing the connection and cursor to the database to ensure all resources are released.
cur.close()
conn.close()
