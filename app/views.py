"""
views.py
"""

from flask import render_template, request, session

from app import app, users
user = users.User()

@app.route('/', methods=['GET', 'POST'])
def signup():
    """
    Function returns signup.html
    """
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']

        txt = user.createuser(email, username, password, cpassword)
        if txt == "Registration successful":
            return render_template("index.html", resp=txt)
        else:
            return render_template("signup.html", resp=txt)

    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Function returns index.html
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        txt = user.login(username, password)
        if txt == "Welcome! Create a new shopping list":
            if username in session:
                return render_template("dashboard.html")
            else:
                session['username'] = username
                return render_template("dashboard.html")
        elif txt == "Account does not exist.Sign up":
            return render_template("signup.html")
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    """
    Function returns dashboard.html
    """
    return render_template("dashboard.html")
