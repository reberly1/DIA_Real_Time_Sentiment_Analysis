"""
Author: Reed Eberly
Description: A list of function pertaining to the MongoDB portion of the
project's functionality
"""

from pymongo import MongoClient

def check_exists(username, client):
    """
    Description
    Confirms or denies the existance of the username in the MongoDB database

    Parameters
    username:     TYPE: str
                  DESC: username being checked

    client:       TYPE: MongoClient
                  DESC: Connection variable between application and MongoDB

    Returns       True if the username exists in the database
                  False Otherwise
    """
    
    db = client['TwitterDatabase']
    usernames = db['users']

    #Counts number of users with the given username
    result = usernames.count_documents({"username" : username})

    #If there exists a user return True
    if (result > 0):
        return True
    
    #Else return False
    return False


