"""
views.py
"""

from flask import render_template

from app import app

@app.route('/')
def index():
    """
    Function returns signup.html
    """
    return render_template("signup.html")

@app.route('/dashboard')
def dashboard():
    """
    Function returns dashboard.html
    """
    return render_template("dashboard.html")

@app.route('/login')
def login():
    """
    Function returns index.html
    """
    return render_template("index.html")
