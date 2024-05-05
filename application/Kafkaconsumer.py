
import json 
from kafka import KafkaConsumer
from nlp import sentiment

consumer = KafkaConsumer('twitter', bootstrap_servers='localhost:9092')

for message in consumer:    
    try: 
        #Assumes the message from producer is json 
        data_tweet = json.load(message.value)
        tweet_text = data_tweet.get('tweet_text')
        if tweet_text:
         #Attemps to update neo4j using nlp function 
         update = sentiment(tweet_text)
         print = ("Tweet Update:", update)
        else:
         #will print in terminal if the consumer has not recieved a tweet or error message
         print("message does not contain tweet")
    except Exception as ex:
         print("error processing message:", str(ex))
      