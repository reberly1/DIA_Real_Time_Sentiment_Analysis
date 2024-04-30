from neo4j import GraphDatabase, basic_auth

def insert_tweet(username, tweet):  
      driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "L1r2c3d4!"))
      with driver.session() as session:
            append_hashtag = False
            mentioned_users = []
            hashtags = []
            append_mention = False  
       

            for i in range(len(tweet)): 

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
                  if hashtag: #skips tweet with no hashtags 
                        cipher_Query += f"""
                        MERGE(h:Hashtag {{name: '{hashtag}'}})
                        CREATE (p)-[:TAGS]->(h)
                        """
            session.run(cipher_Query, username=username,tweet=tweet)
       
            return cipher_Query

def reccomend_tweet(tweet_text):
      driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "L1r2c3d4!"))
      
      with driver.session() as session:
                  append_hashtag = False
                  mentioned_users = []
                  hashtags = []
                  append_mention = False  
                 
                  for i in range(len(tweet_text)): 

                        if tweet_text[i] == " ":
                              append_mention = False 
                              append_hashtag = False
                        
                        if append_mention == True:
                              mentioned_users[len(mentioned_users) - 1] += tweet_text[i]
                        
                        if append_hashtag == True:
                              hashtags[len(hashtags) - 1] += tweet_text[i]
                        
                        if tweet_text[i] == '@':
                              append_mention = True
                              mentioned_users.append("")
                        
                        if tweet_text[i] == '#':
                              append_hashtag = True
                              hashtags.append("")
                 
                  reccomend_query =  """
                        MATCH (h:Hashtag)<-[:TAGS]-(t:Tweet)<-[:POSTS]-(u:User)
                        WHERE h.name IN $hashtags OR u.screen_name IN $mentions
                        RETURN t.text AS tweet_text, u.screen_name AS user
                        LIMIT 10
                  """
                 
                  tweetresult = session.run(reccomend_query, hashtags=hashtags, mentions=mentioned_users)
                  reccomendationsquery = [(record["user"], record["tweet_text"]) for record in tweetresult]
                  return reccomendationsquery
  
if __name__ == "__main__":
      text = "How about this? @datacentretimes #data"
      reccomendations = reccomend_tweet(text)
      print("These are the reccomendations:", reccomendations)

      text = "How about this? #graphs"
      reccomendations = reccomend_tweet(text)
      print("These are the reccomendations:", reccomendations)

      text = "How about this? @neo4j"
      reccomendations = reccomend_tweet(text)
      print("These are the reccomendations:", reccomendations)

