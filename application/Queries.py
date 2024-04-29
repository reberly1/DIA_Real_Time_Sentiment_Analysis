from neo4j import GraphDatabase, basic_auth

#Graph Insertion 
def insert_tweet(username, tweet):  
      driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "L1r2c3d4!"))
      with driver.session() as session:
            append_hashtag = False
            mentioned_users = []
            hashtags = []
            append_mention = False  
            
            #May have to change to for i in range(len(tweet) - 1): if an out of bounds error occurs
            for i in range(len(tweet)): 
            #if a space is detected, that means any hashtags or mentions have ended
            #may have to tweak space check condition
                  if tweet[i] == " ":
                        append_mention = False 
                        append_hashtag = False
                  
                  if append_mention == True:
                        mentioned_users[len(mentioned_users) - 1] += tweet[i]
                  
                  if append_hashtag == True:
                        hashtags[len(hashtags) - 1] += tweet[i]
                  
                  if tweet[i] == '@':
                        append_mention = True
                        mentioned_users.append("")
                  
                  if tweet[i] == '#':
                        append_hashtag = True
                        hashtags.append("")

                  cipher_Query = """
                  MATCH (u: User {screen_name: $username})
                  CREATE (p:Tweet {text: $tweet})
                  CREATE (u)-[:POSTS]->(p)
                  """ 
                  for  mentioned_user in mentioned_users:
                        if mentioned_user: #skip empty mentions also, makes sure every user is unique
                              cipher_Query += f"""
                              MERGE(mu: User {{screen_name: '{mentioned_user}'}})
                              CREATE (p)-[:MENTIONS]->(mu)
                              """
                  for hashtag in hashtags: 
                        if hashtag: #skip no hashtags 
                              cipher_Query += f"""
                              MERGE(h:Hashtag {{name: '{hashtag}'}})
                              CREATE (p)-[:CONTAINS]->(h)
                              """
                  
            session.run(cipher_Query, username=username,tweet=tweet)
                  
            return cipher_Query

def reccomend_tweet(tweeter):
      driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "L1r2c3d4!"))
      with driver.session() as session:
            reccomend_query = """
            MATCH (u:User {screen_name: $username})-[:POSTS]->(:Tweet)-[:CONTAINS]->(h:Hashtag)
            WITH u, COLLECT(DISTINCT h.name) AS hashtags
            MATCH (other:User) -[:POSTS]->(t:Tweet)-[:CONTAINS]->(h2:Hashtag)
            WHERE other <> u AND h2.name IN hashtags 
            RETURN other.name AS user, t.text AS tweet_text
            """
            tweetresult = session.run(reccomend_query, username=tweeter)
            reccomendationsquery = [(record["user"], record["tweet_text"]) for record in tweetresult]
            return reccomendationsquery

if __name__ == "__main__":
      username = "neo4j"
      text = "How about this? @28_fireball #data"
      Insertion = insert_tweet(username, text)
      print(Insertion)
      reccomendations = reccomend_tweet(username)
      print("These are the reccomendations:", reccomendations)