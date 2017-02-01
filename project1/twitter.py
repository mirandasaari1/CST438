#downloads home TL tweets and print to console
import tweepy
import render_template
import flask
import session
#import 'tauthorization.php' #correct import??

#are the Oauth steps needed??

app = flask.Flask(__name__)
consumer_key = 	"bgsi3dhSOFgSv7smGbbqviIT9"
consumer_secret = 	"tqg7y6GjOSzkTV3i0g56XkeORUaVanj7w0OCVSZmz694bzzro9"
access_token = 	"399817303-XsV9PzDJ83iHtjYWNwjxEiHjOIg7BRI1hkoM2vNl"
access_token_secret = 	"MsUvIwYuFkuLZZYRZijydLJQeU96bY8wJEuMPdchVRVDq"

@app.route('/')

def page():
    #add callback url since being supplied dynamically, do i need?
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    
    #prints tweets
    #for tweet in public_tweets:
        #print tweet.text
 
    #get the user from twitter   
    user = api.get_user('twitter')
    #get the tweet from twitter
    tweet = api.get_tweet('twitter')
    #get attribution link
    at_link = api.get_attribution_link('twitter')

#some examples of model helper methods
#print user.screen_name
#print user.followers_count
#for friend in user.friends():
#   print friend.screen_name
   
    #fetch request token
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'
    #stores request token in a session
    session.set('request_token', auth.request_token)

    #exchanging acess token for request token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    token = session.get('request_token')
    session.delete('request_token')
    auth.request_token = token

#dont need since not callback?
    #try:
    #    auth.get_access_token(verifier)
    #except tweepy.TweepError:
    #    print 'Error! Failed to get access token.'
    
    #store these vals
    auth.access_token
    auth.access_token_secret
    
    #access these in DB file to rebuild Oauth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(key, secret)
    
    #Oauth handler with access
    api = tweepy.API(auth)
    api.update_status('tweepy + oauth!')