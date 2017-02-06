import tweepy
import flask
from random import shuffle

app = flask.Flask(__name__)
consumer_key = 	"bgsi3dhSOFgSv7smGbbqviIT9"
consumer_secret = 	"tqg7y6GjOSzkTV3i0g56XkeORUaVanj7w0OCVSZmz694bzzro9"
access_token = 	"399817303-XsV9PzDJ83iHtjYWNwjxEiHjOIg7BRI1hkoM2vNl"
access_token_secret = 	"MsUvIwYuFkuLZZYRZijydLJQeU96bY8wJEuMPdchVRVDq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

    
    
for user in randomTweet:
    user = user.screen_name
    tweet = user.text
    at_link = user.url
    
def randomizeTweets():
    Tweet = api.search("disneyquotes", lang = "en")
    randomTweet = random.shuffle(Tweet) 
    chosenTweet = randomTweet[0]
    return chosenTweet
    
    #quoteAPI=json.dumps(quoteAPI._json)