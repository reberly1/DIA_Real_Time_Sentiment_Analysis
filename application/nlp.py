from neo4j import GraphDatabase, basic_auth
from textblob import TextBlob

def sentiment(tweet):
    polarity = TextBlob(tweet).sentiment.polarity

    sentiment = ""
    if polarity < 0:
        sentiment = "Negative"
    elif polarity > 0:
        sentiment = "Positive"
    else:
        sentiment = 'Neutral'

    cipher_query = """
    MATCH (t:Tweet)
    WHERE t.text = $tweet
    SET t.sentiment = $sentiment
    """

    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "Irunfast3***"))

    driver.execute_query(cipher_query, tweet=tweet, sentiment=sentiment, database_="neo4j")

    return

