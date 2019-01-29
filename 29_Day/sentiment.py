# dependencies
from tweepy.streaming import StreamListener  # class to get the tweets from API
from tweepy import OAuthHandler  # to authenticate with Twitter
from tweepy import Stream
import twitter_credential


class StdOutListener(StreamListener):
    def on_data(self, data):  # listener for tweets  ## this are class  method and we override it
        print(data)
        return True

    def on_error(self, status):  # if any error happen the its print the error ststus
        print(status)


if __name__ == "__main__":
    listener = StdOutListener()  # creating object
    auth = OAuthHandler(twitter_credential.Consumer_key, twitter_credential.Consumer_secret_key)  #pass the credentials from twitter.py file
    auth.set_access_token(twitter_credential.Access_token,twitter_credential.Access_token_secret)
    stream = Stream(auth, listener)

    stream.filter(track=['Arup Das','elon musk'])  # this filter is for what we need if any this happen like is name then it will show
    # Output will be in JSON format

