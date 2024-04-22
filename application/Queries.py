from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "Irunfast3***"))

#Graph Insertion 
def insert_tweet(username, tweet, mentioned_users=[], hashtags=[]):   
 cipher_Query = """
MATCH (u: User {name: $username})
CREATE (p:Tweet {text: $tweet})
CREATE (u)-[:POSTED]->(p)
""" 
 for index, mentioned_user in enumerate(mentioned_users):
        cipher_Query += f"""
        MERGE(mu{index}: User {{name: '{mentioned_user}'}})
        CREATE (p)-[:MENTIONS]->(mu{index})
        """
         
 for hashtag in hashtags:
        cipher_Query += f"""
        MERGE(h:Hashtag {{name: '{hashtag}'}})
        CREATE (p)-[:CONTAINS]->(h)
        """
 return cipher_Query


Username = "R Sanjabi"
Tweet = "Test #Neo4j is good! @Fireball28 @Holly"
users_mentioned = ["Fireball 28", "Holly"]
Hashtags = ["#Neo4j"]
cypher_query = insert_tweet(Username, Tweet, users_mentioned, Hashtags)


with driver.session() as session:
    tweet1result = session.run(cypher_query, username=Username,tweet=Tweet)
    print(tweet1result)
    

