from flask import Flask, render_template, request, session
from pymongo import MongoClient
from mongo import *
from Queries import insert_tweet, reccomend_tweet

app = Flask(__name__)
app.secret_key = "Dummy Key For Debugging Purposes"

@app.route('/', methods=['GET','POST'])
def tweet():
    if 'username' not in session:
        session['username'] = ""
        message = "Please login before posting a tweet"
        return render_template('tweet.html', title="Tweet", message=message)
    
    username = session['username']
    
    if request.method == 'POST' and username != "":
        tweet = request.form['tweet']
        session['tweet'] = tweet
        print(insert_tweet(username, tweet))
        message = "Tweet Sucessfully Posted"
        return render_template('tweet.html', title="Tweet", tweet=tweet, username=username, message=message)
    
    return render_template('tweet.html', title="Tweet", username=username)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Connects to the MongoDB database via MongoClient
        client = MongoClient(host=["mongodb://localhost:27017/"])
        
        username = request.form['username']
        message = ""

        if (check_exists(username, client)):
            session['username'] = username
            message = "User has been logged in as " + username
        else:
            message = "User was not found try another username"

        return render_template('login.html',title='Login', username=username, message=message)
    
    return render_template('login.html',title='Login')

@app.route('/recommend')
def recommend():
    if 'username' in session:
        username = session['username']
        recommendation = reccomend_tweet(username)
        return render_template('recommend.html',title='Recommended', recommendation=recommendation, length=len(recommendation))
