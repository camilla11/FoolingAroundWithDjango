import urllib2, urllib
import tweepy
import csv, re
#install tweepy!!!

def find_tweets(topic):

    # The consumer keys can be found on your application's Details
    # page located at https://dev.twitter.com/apps (under "OAuth settings")
    consumer_key="Prhl7bg2fKDLFn5DjugCgZuQB"
    consumer_secret="yPbtDnKABdYw8e8Kx8QrdQChxdv3zvdKJKYNJRGPf8xI82JQtk"

    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located
    # under "Your access token")
    access_token="349880230-N3ggmI5uJ9J8w3VT7hFTFuXXGqeRIz5OfJNhH5EE"
    access_token_secret="LVXK5ZXAZCwwMTsTISAYsyv9JBFJct8G13tvUtA6v6GKd"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    print "Looking..."
    word_list = topic.wordtotrack_set.all()    
    user_list = topic.usertotrack_set.all()
    print word_list
    print user_list
    
    matchingtweets = ""
    for user in user_list:
        print user.user_text
        public_tweets = api.user_timeline(str(user.user_text), count=100)
        for tweet in public_tweets:
            tweetinfo = tweet.text.encode('UTF-8')
            for word in word_list:
                print word.word_text
                if str(word.word_text) in tweetinfo.lower():
                    matchingtweets += str(user.user_text)+ " tweeted '"+ str(word.word_text) + "' in: "+ str(tweetinfo) + "\n\n ----- \n\n"

    print matchingtweets
    return matchingtweets
    
    
    
if __name__ == '__main__':
    save_tweets()