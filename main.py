
print("Hi From Workflow 1")

# import the module
import os
import csv
import tweepy
import psycopg2
from pytz import timezone
from datetime import datetime

ACCESS_KEY = os.environ["ACCESS_KEY"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]


# Create a new CSV file called "example.csv"
with open("twitter_trends.csv", "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Name", "Age", "City"])
    
    # Write some data rows
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])


print("Hi From Workflow 2")
