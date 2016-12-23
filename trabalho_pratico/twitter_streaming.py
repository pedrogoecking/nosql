from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient   

ckey = 'Et95tH8EG5jP3IUc2KXSA1uik'
csecret = 'jnuA0ser9t37WA7eYavPr1ud8KF9oYfOop1qKcEHNpFyie0iCr'
atoken = '808007428663087104-3bqlBZJsiyiqHXP4el0LJuGzwdhPSgS'
asecret = 'FTZxWjEFRvHAyr3kK5f2o882o7mHZwZTp33cfSFEVj4qM'

class listener(StreamListener):
    def on_data(self, data):
        tweet=json.loads(data)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,
        "id_str":id_str,
        "text":text,}
        tweetind=collection.insert_one(obj).inserted_id
        print obj
        return True
    def on_error(self, status):
        print status


client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.nosqlclass
collection = db.test_collection 

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["berlin","aleppo","terrorism","muslim","attack","russian","syria","turkey", 
                            "usa","united states","terrorist","death", "dead","die","army","twitter","russia"])