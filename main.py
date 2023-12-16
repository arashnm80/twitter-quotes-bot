from functions import *

if __name__ == "__main__":
    # try at most 10 times to make sure tweet characters are not too much
    for i in range(10):
        tweet_text = get_tweet_text()
        if len(tweet_text) > 280:
            print("tweet text more than 280 characters")
        else:
            post_tweet(tweet_text)
            break