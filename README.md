# twitterTrends
This repository contains a Python script that extracts trending Twitter topics for India, USA, and worldwide and inserts them into a database hosted on ElephantSQL.

Requirements
Python 3.x
Tweepy (Python library for accessing the Twitter API)
psycopg2 (Python library for interacting with PostgreSQL databases)
Access to an ElephantSQL database
Setup
Clone the repository
Copy code
git clone https://github.com/<username>/twitterTrends.git
Install the required libraries
Copy code
pip install -r requirements.txt
Create a new application on Twitter Developer to obtain the necessary API keys and access tokens.
Add the API keys and access tokens to the script in the appropriate variables.
Update the database connection information in the script, including the host, port, database name, username, and password.
Run the script
Copy code
python twitterTrends.py
Usage
The script will run continuously, extracting trending topics for India, USA, and worldwide every 15 minutes and inserting them into the specified ElephantSQL database. The database table will contain columns for the trend name, the location, and the timestamp of when the trend was extracted.

Note
The script is set to extract the trending topics every 15 minutes, you can change the time as per your requirement in the script.
The script uses the WOEID (Where On Earth ID) for India, USA and worldwide to extract the trending topics.
Contributing
If you find any bugs or have any suggestions for improvements, please open an issue or submit a pull request.
