import tweepy
import requests
from requests.exceptions import HTTPError

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

# Create API object
api = tweepy.API(auth)

harga = 0
try:
    response = requests.get('https://jibs.my.id/api/harga_komoditas')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(type(jsonResponse["national_commodity_price"]["Daging Ayam"]))
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

# Create a tweet
# api.update_status("Hello Tweepy")