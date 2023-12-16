from variables import *

import tweepy
import requests
import json

def post_tweet(tweet_text):

    client = tweepy.Client(
        bearer_token=TWITTER_BEARER_TOKEN,
        consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

    response = client.create_tweet(
        text = tweet_text
    )

    print(response.data)
    print(f"https://twitter.com/user/status/{response.data['id']}")

def get_tweet_text():
    # # if we need to specify category:
    # category = 'happiness'
    # api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_KEY})
    if response.status_code == requests.codes.ok:
        # Parse the JSON string
        data = json.loads(response.text)

        quote = data[0]["quote"]
        author = data[0]["author"]
        category = data[0]["category"]

        output_text = f"\"{quote}\"\n\n{author}"
        return output_text
    else:
        print("Error:", response.status_code, response.text)