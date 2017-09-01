"""
Initializes application
"""
from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
# secret key for Session
app.secret_key = '\xacd\xf3\xe3\xb7\x06>\x86\x1d\x0b\x9c/\xfc)\xbd\xc57\x14\x80\xbc\xc2\x1d\x97h'

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
