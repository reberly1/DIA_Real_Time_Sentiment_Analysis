from flask import Flask, render_template, request, session
from pymongo import MongoClient
from mongo import *

app = Flask(__name__)
app.secret_key = "Dummy Key For Debugging Purposes"

@app.route('/', methods=['GET','POST'])
def tweet():
    if 'username' not in session:
        session['username'] = ""
    username = session['username']
    message = "Tweet Rejected, Please login before posting a tweet"

    if request.method == 'POST' and username != "":
        tweet = request.form['tweet']
        message = "Tweet Sucessfully Posted"
        return render_template('tweet.html', title="Tweet", tweet=tweet, username=username, message=message)
    return render_template('tweet.html', title="Tweet", username=username, message=message)

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
    return render_template('recommend.html',title='Recommended')
