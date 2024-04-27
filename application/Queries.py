from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "Irunfast3***"))
#Graph Insertion 
#Graph Insertion 
def insert_tweet(username, tweet):   
       mentioned_users = []
       hashtags = []
       append_mention = False
       append_hashtag = False
#May have to change to for i in range(len(tweet) - 1): if an out of bounds error occurs
       for i in range(len(tweet)): 
	#if a space is detected, that means any hashtags or mentions have ended
	#may have to tweak space check condition
              if tweet[i] == " ":
                     append_mention = False
                     append_hashtag = False
              
              if append_mention == True:
                    mentioned_users[len(mentioned_users) - 1] += tweet[i]
              
              if append_mention == True:
                    hashtags[len(hashtags) - 1] += tweet[i]
              
              if tweet[i] == '@':
                    append_mention = True
                    mentioned_users.append("")
              
              if tweet[i] == '#':
                   append_hashtag = True
                   hashtags.append("")		

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




def reccomend_tweet(tweeter):
  with driver.session() as session:
    reccomend_query = """
    MATCH (u:User {name: $username})-[:POSTS]->(:Tweet)-[:CONTAINS]->(h:Hashtag)
    WITH COLLECT(DISTINCT h.name) AS hashtags
    MATCH (other:User) -[:POSTS]->(:Tweet)-[:CONTAINS]->(h2:Hashtag)
    WHERE other <> u AND h2.name IN hashtags 
    RETURN other.name AS user, tweet.text AS tweet_text
    """
    tweetresult = session.run(reccomend_query, username=tweeter)
    reccomendationsquery = [(record["user"], record["tweet_text"]) for record in tweetresult]
    return reccomendationsquery


Username = "Stanley Bishop"
reccomendations =  reccomend_tweet[Username]
print("These are the reccomendations:", reccomendations)
     
     


