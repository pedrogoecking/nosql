from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

import json

access_token = "808007428663087104-3bqlBZJsiyiqHXP4el0LJuGzwdhPSgS"

access_token_secret = "FTZxWjEFRvHAyr3kK5f2o882o7mHZwZTp33cfSFEVj4qM"

consumer_key = "Et95tH8EG5jP3IUc2KXSA1uik"

consumer_secret = "jnuA0ser9t37WA7eYavPr1ud8KF9oYfOop1qKcEHNpFyie0iCr"

 

# Defining listener class for getting the streamingclass StdOutListener(StreamListener):

def on_data(self, testdata2):           

#Retrieving the details like Id, tweeted text and created at.

        tweet=json.loads(testdata2)

        created_at = tweet["created_at"]

        id_str = tweet["id_str"]

        text = tweet["text"]

        obj = {"created_at":created_at,"id_str":id_str,"text":text,}

        tweetind=collection.insert_one(obj).inserted_id

        print obj

return True

def on_error(self, status):

        print status

    if __name__ == '__main__':

 

        #This handles Twitter authetification and the connection to Twitter Streaming AP

        l = StdOutListener()

        auth = OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, l)

 

 # Below code  is for making connection with mongoDB

    from pymongo import MongoClient   

    client = MongoClient()

    client = MongoClient('localhost', 27017)

    db = client.test_database

    collection = db.test_collection 

#This line filter Twitter Streams to capture data by the keywords: 'India'

     stream.filter(track=['Amor'])