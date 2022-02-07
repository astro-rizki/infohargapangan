import tweepy
import requests
import datetime
from requests.exceptions import HTTPError
from pandas import json_normalize
from flask import Flask
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
# Create API object
api = tweepy.API(auth)

CATEGORY = ["cat-1", "cat-2", "cat-3", "cat-4", "cat-5", "cat-6", "cat-7", "cat-8", "cat-9", "cat-10"]
CATEGORY_NAME = ["Beras", "Daging Ayam", "Daging Sapi", "Telur Ayam", "Bawang Merah", "Bawang Putih", "Cabai Merah", "Cabai Rawit", "Minyak Goreng", "Gula Pasir"]
DATE = datetime.datetime.now()
DATE = DATE.strftime("%d-%m-%Y")
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    try:
        for i in range(0, len(CATEGORY)):
            print(i)
            como = requests.get('https://hargapangan.id/index.php?option=com_gtpihps&price_type_id=1&data_type=price&date='+DATE+'&task=json.getData&commodity_id='+CATEGORY[i])
            como.raise_for_status()
            como = como.json()["tableData"]
            como = json_normalize(como)
            como.sort_values('value')
            # Create a tweet
            api.update_status(CATEGORY_NAME[i])
        
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return 'OK'
  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()