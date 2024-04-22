from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "Dummy Key For Debugging Purposes"

@app.route('/', methods=['GET','POST'])
def tweet():
    if request.method == 'POST':
        tweet = request.form['tweet']
        return render_template('tweet.html', title="Tweet", tweet=tweet)
    return render_template('tweet.html', title="Tweet")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('login.html',title='Login', username=username, password=password)
    
    return render_template('login.html',title='Login')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html',title='Recommended')