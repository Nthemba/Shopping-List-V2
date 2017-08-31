"""
views.py
"""

from flask import render_template

from app import app

@app.route('/')
def index():
    """
    Function returns index.html
    """
    return render_template("index.html")

@app.route('/about')
def about():
    """
    Function returns inaboutdex.html
    """
    return render_template("about.html")
