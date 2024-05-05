
from kafka import KafkaProducer
from app import tweet

producer = KafkaProducer(bootstrap_servers='localhost:9092')

app = tweet()
KafkaProducertopic = "twitter"

def send_tweet(tweet_text):
    try:
        #Sends the tweet to twitter topic
        producer.send(KafkaProducertopic, value=tweet_text)
        producer.flush()  
        #Confirms if the message has been sent to the topic 
        print("The tweet has been sent to the topic:", KafkaProducertopic)
    except Exception as error:
        #Displays if there was an error sending the tweet
        print("There was an error sending the tweet to the topic:", KafkaProducertopic)

if __name__ == "__main__":
        tweet_text = app
        send_tweet(tweet_text)
