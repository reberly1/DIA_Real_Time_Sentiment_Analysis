from neo4j import GraphDatabase, basic_auth
from pymongo import MongoClient

#Connects to the neo4j database via bolt driver
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "L1r2c3d4!"))

#Connects to the MongoDB database via MongoClient
client = MongoClient(host=["mongodb://localhost:27017/"])

#Test Query to Confirm basic functionality of neo4j
query = "MATCH (n:User) RETURN n"

results, summary, keys = driver.execute_query(query, database_="neo4j")

mongo_data = {}
for node in results:
    dictionary = node.data()

    mongo_data[dictionary['n']['name']] = dictionary["n"]['name']

#Extract the tweet text from all tweets
query_1 = "MATCH (t:Tweet) WHERE t.text IS NOT NULL Return t"

results, summary, keys = driver.execute_query(query_1, database_="neo4j")

mongo_tweets = {}
for node in results:
    dictionary = node.data()
    mongo_tweets[dictionary['t']['id_str']] = dictionary['t']['text']

#Completely Deletes the database for test purposes
client.drop_database('TwitterDatabase')

#Create a database within mongodb with a users and tweets collection
db = client['TwitterDatabase']
users = db['users']
tweets = db['tweets']

#Inserts the users' name data into MongoDB
for key in mongo_data:
    users.insert_one({key: mongo_data[key]})

#Inserts all tweet text into the tweets collection
for key in mongo_tweets:
    tweets.insert_one({key: mongo_tweets[key]})
