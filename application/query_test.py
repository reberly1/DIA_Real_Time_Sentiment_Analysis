"""
Author: Reed Eberly
Description: A testing suite to confirm that the neo4j queries are
working as intended using test scenarios
"""

from Queries import *

if __name__ == "__main__":
#Insert Tweet Function Test Scenarios

    #Scenario 1, standard tweet with embedded hashtags
    name = 'R Sanjabi'
    tweet = 'Using #github helps you revert changes you want to undo #education'

    #insert_tweet(name, tweet)

    #Scenario 2, standard tweet with embedded hashtags and mentions
    #Note this uses R Sanjabi's screen name not his actual name
    #This is because on Twitter, mentions will go to the person's screen name
    #Not their actual name that we use for 
    name_1 = 'Stanley Bishop'
    tweet_1 = 'Hey @r_sanjabi, I am hosting a new #podcast on graph databases if you want to join #graphs.'

    #insert_tweet(name_1, tweet_1)

#Recommedation Function Test Scenarios
    
    #Scenario 3, get Stanley's recommendations
    #Should return at most 5 users either who use the same hashtags or have been mentioned
    #Should return 1 tweet from each user who was recommended
    #This should be in the form of a tuple list with format
    #[(username, tweet),(username_2, tweet_2),etc.]
    #Where username and tweet are both strings 
    #result = recommend_tweet('Stanley Bishop')


