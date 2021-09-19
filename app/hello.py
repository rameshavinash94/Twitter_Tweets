#Create a class Twitter for all operations
class Twitter:        

        #intialize auth and necessary tokens for api
        def __init__(self):
                import tweepy
                self.auth = tweepy.OAuthHandler("EJ4lKn9eUeILtMqogH2iZfKYj", "0DXKL5x2MPYLEKgdClasOi1xG6IX0nBsWfPQhwEcKJJL2nBJYn")
                self.auth.set_access_token("1438542318827544579-RgJGMuZRIH4yvXAD1VV4bWn4lv0lKx", "oN7cw127YZ7NeC7Xk7485dTIFEgQC9924ArOaxXLVfU1c")
                self.api = tweepy.API(self.auth)
                self.cursor=tweepy.Cursor(self.api.user_timeline)
                self.temp=[]
                self.my_tweets=[]

#create a tweet
        def create_tweets(self,tweets):
                self.api.update_status(tweets)
                return "tweet posted successfully"

#Show user tweets
        def view_tweets(self,show='1'):
                self.my_tweets = self.api.user_timeline()               
                if (show != 'All'):
                        for x in self.my_tweets:
                                self.temp.append(str(x.text))
                        return self.temp[:int(show)]
                else:
                        for x in self.my_tweets:
                                self.temp.append(str(x.text))
                        return self.temp[:]

#delete tweets
#removed delete script
