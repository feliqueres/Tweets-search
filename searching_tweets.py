import tweepy
import json


with open('config.json') as json_file:
    config_data = json.load(json_file)

    consumer_key = config_data['consumer_key']
    consumer_secret = config_data['consumer_secret']
    access_token = config_data['access_token']
    access_token_secret = config_data['access_token_secret']
    twitter_account = config_data['twitter_account_to_search']

    words = config_data['words']

tweets = []
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

iterator = 0
while True:
    result = api.user_timeline(id=twitter_account, count=200, page=iterator, include_rts=1)

    if len(result) is 0:
        break

    tweets += result
    iterator += 1

for tweet in tweets:
    for word in words:
        if word.lower() in tweet.text.lower():
            print('Tweet:\t' + tweet.text)
            print('Date:\t' + tweet.created_at.strftime('%d/%m/%Y'))

            print('URL:\thttps://twitter.com/' + twitter_account + '/status/' + str(tweet.id)+"\n")
