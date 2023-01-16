# TwitterTrends

TwitterTrends is a repository that contains the Python code to extract trending topics from Twitter for India, USA and worldwide and insert them into a database hosted on ElephantSQL (*Free Tier*). This repository is useful for anyone looking to quickly extract trending topics from Twitter and store them in a database.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Psycopg2 library (For POTSGRES Database)
- Tweepy (3.9.0 or higher)
- Access to a Twitter API key
- Access to an ElephantSQL or any Database

## Installation

To install the TwitterTrends repository, simply clone or download it from the GitHub repository:
```
git clone https://github.com/305kishan/TwitterTrends.git
```

Install the required packages: 
```
pip install -r requirements.txt
```

## Usage

The TwitterTrends repository contains the code to extract trending topics from Twitter for India, USA and worldwide and insert them into a database hosted on Elephantsql.

The code uses the Psycopg2 library to connect to the Elephantsql database.

To execute the code, simply run the following command in your terminal:

```
python3 main.py
```
The script will extract the trending topics and insert them into the specified ElephantSQL database.

## Contributing
If you want to contribute to this repository, please submit a pull request with your suggested changes.
