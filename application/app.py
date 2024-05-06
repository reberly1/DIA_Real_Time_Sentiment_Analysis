from flask import Flask, render_template, request, session
from pymongo import MongoClient
from mongo import *
from Queries import insert_tweet, reccomend_tweet
from nlp import sentiment

app = Flask(__name__)
app.secret_key = "Dummy Key For Debugging Purposes"

@app.route('/', methods=['GET','POST'])
def tweet():
    #If user is not logged in return error message
    if 'username' not in session:
        session['username'] = ""
        message = "Please login before posting a tweet"
        return render_template('tweet.html', title="Tweet", message=message)
    
    username = session['username']
    
    #If user is logged in and tweets, insert the tweet in neo4j, upload tweet to mongodb
    if request.method == 'POST' and username != "":
        tweet = request.form['tweet']
        session['tweet'] = tweet
        
        #Inserts tweet into neo4j
        insert_tweet(username, tweet)
        
        #Uploads tweet to mongodb
        upload_tweet(tweet, username)
        
        #Apply nlp and update the tweet based on the sentiment
        sentiment(tweet)
        message = "Tweet Sucessfully Posted"
        return render_template('tweet.html', title="Tweet", username=username, message=message)
    
    #If user is not logged in and tries to tweet return error message
    elif request.method == 'POST':
        message = "Please login before posting a tweet"
        return render_template('tweet.html', title="Tweet", username=username, message=message)
    
    return render_template('tweet.html', title="Tweet", username=username)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        client = MongoClient(host=["mongodb://localhost:27017/"])
        
        username = request.form['username']
        password = request.form['password']
        message = ""

        #Check credentials and log them in if credentials are valid
        if (check_exists(username, password)):
            session['username'] = username
            message = "User has been logged in as " + username
        else:
            message = "User could not be logged in, check username and password"

        return render_template('login.html',title='Login', username=username, message=message)
    
    return render_template('login.html',title='Login')

@app.route('/recommend')
def recommend():
    #Shows the user recommendations based on the tweet they most recently posted
    if 'tweet' in session:
        tweet = session['tweet']
        recommendation = reccomend_tweet(tweet)
        return render_template('recommend.html',title='Recommended', recommendation=recommendation, length=len(recommendation))
    else:
        return render_template('recommend.html',title='Recommended', message="Please post a tweet to receive recommendations")
    
    
