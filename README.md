# DIA Real Time Sentiment Analysis

## Overview 
The project implementation was created to address the issues of traditional recommendation systems which became obsolete upon the introduction of big data conditions that social media platforms manage on a daily basis. These issues include the system’s inability to handle the introduction of new data into recommendations as it is logged as well as the inability to efficiently query with the high prevalence of many to many relationships. To address these issues, the project uses a graph database Neo4j that specializes in expressing many to many relationships in a way that makes them more effective and efficient to store and query. Additionally, a Kafka pipeline is introduced to stream the tweet data so that further operations can be performed such as real time natural language processing can be applied to update the user’s tweet as soon as it’s posted. To facilitate future batch processing operations on user tweets, a document store MongoDB is introduced to store tweets as they are posted. Lastly, using MongoDB and Flask, the user is authenticated through their entered credentials and through the user interface they’re able to post tweets and receive recommendations based on the tweet they have posted.

## Important Files
app.py: Python file involving flask application interacting with MongoDB to interact with in order to insert tweets and conduct recommendations based on those tweets. 

Queries.py: Python files that invlove recommendation and insertion querys from neo4j python bolt driver for neo4j.

Load.py: Loads neo4j database users and tweets into MongoDB database.

Login.hmtl: Front-end UI for Login Page which communicates with MongoDB to authenticate the user by requiring a password which is "Password123".

Recommend.html: Front-end UI for Recommendations page which displays the reccomendations for the inserted tweets based on mentioned users and hashtags.  

Tweet.html: Front-end UI for inserting tweets while being logged in as a specific user.

## Prerequisites
-Python 3.12.2 

-MongoDB Compass

-MongoDB Community Server 7.0

-Neo4j Desktop

-Flask

## Setup and Installation 
1. Install python 3.12.2 and to PATH in environment variables
2. Install Apache Kafka 3.7.0 [https://kafka.apache.org/downloads](url)
3. Install MongoDB Compass [https://www.mongodb.com/try/download/shell](url)
## Steps to deploy the flask application
  ### Through VS Code:
1. #### Create virutal environment
2. #### run `pip install Pymongo`
4. ####  run ` pip install flask`
5. #### type `cd application` to navigate to the application directory
6. #### type `run flask` to deploy flask application

## List of Dependencies 
#### blinker: 
This module is responsible for providinf a fast Python dispatching system 
#### certifi: 
A python module that provides Mozilla's CA Bundle 
#### charset-normalizer: 
Enables the user to read tect from charset names 
#### click: 
Module for creating CLI
#### colorama: 
colored terminal text
#### dnspython: 
DNS toolkit
#### Flask: 
Web application framework 
#### idna: 
Internationalized Domain Names in Applications module 
#### itsdangerous: 
Muliple helpers pass data to untrusted environments in a secure manner 
#### Jinja2:
Template engine for python 
#### joblib 
Tools th
#### MarkupSafe: 
Enables HTML/XML Markup safe string for python 
#### neo4j: 
Python bolt driver for neo4j
#### ntlk: 
Natural Language Toolkit 
#### pymongo: 
Python driver for MongoDB
#### pytz: 
World timezone definitions
#### textblob:
Open-source library for processing textual data in Python
#### tdqm: 
progress bar for python and CLI
#### urllib3: 
Python HTTP client 
#### Werkzeyg:
Web application library 
