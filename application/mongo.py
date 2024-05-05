"""
Author: Reed Eberly
Description: A list of function pertaining to the MongoDB portion of the
project's functionality
"""

from pymongo import MongoClient

def check_exists(username, password):
    """
    Description
    Confirms or denies the existance of the username in the MongoDB database

    Parameters
    username:     TYPE: str
                  DESC: username being checked

    password:     TYPE: str
                  DESC: password for account

    Returns       True if the username exists in the database
                  False Otherwise
    """
    client = MongoClient(host=["mongodb://localhost:27017/"])
    db = client['TwitterDatabase']
    usernames = db['users']

    #Counts number of users with the given username and password
    result = usernames.count_documents({"username" : username, "password" : password})

    #If there exists a user return True
    if (result > 0):
        return True
    
    #Else return False
    return False

def upload_tweet(tweet, username):
    """
    Description
    Uploads tweet to mongodb for batch processing

    Parameters
    tweet:        TYPE: str
                  DESC: tweet string being stored for batch processing

    username:     TYPE: str
                  DESC: username of the person who posted the tweet

    Returns
    """
    client = MongoClient(host=["mongodb://localhost:27017/"])
    db = client['TwitterDatabase']
    tweets = db['tweets']

    #Checks for duplicates
    result = tweets.count_documents({"author" : username, "tweet" : tweet})

    if result:
        return False

    tweets.insert_one({'author': username, 'tweet': tweet})
    return True

