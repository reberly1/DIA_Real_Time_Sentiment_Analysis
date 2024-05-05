from neo4j import GraphDatabase, basic_auth
from textblob import TextBlob

def sentiment(tweet):
    """
    Description
    Performs sentiment analysis on the tweet and updates the tweet in neo4j

    Parameters
    tweet:        TYPE: str
                  DESC: tweet being analyzed 

    Returns       None
    """
    
    polarity = TextBlob(tweet).sentiment.polarity

    #Collects the sentiment from the polarity
    sentiment = ""
    if polarity < 0:
        sentiment = "Negative"
    elif polarity > 0:
        sentiment = "Positive"
    else:
        sentiment = 'Neutral'

    #Updates the tweet sentiment
    cipher_query = """
    MATCH (t:Tweet)
    WHERE t.text = $tweet
    SET t.sentiment = $sentiment
    """

    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "L1r2c3d4!"))

    driver.execute_query(cipher_query, tweet=tweet, sentiment=sentiment, database_="neo4j")

    return

