# impor the flask class forom the flask module
from flask import Flask, render_template, request, url_for, \
    redirect, session, flash

from flask_sqlalchemy import SQLAlchemy
from functools import wraps


# create the aplication object
app = Flask(__name__)

# config 
import os
app.config.from_object(os.environ['APP_SETTINGS'])

#create the sqlalchemy object
db = SQLAlchemy(app)

# this import needs to be after the db, otherwise we would have some problems when creating the db
from models import *

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
# we need reformulate the function
# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('home/index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template('home/welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash("You are just logged in!")
            return redirect(url_for('home'))
    return render_template('user/login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You are just logged out!")
    return redirect(url_for('welcome'))

#connect database function


if __name__ == '__main__':
    app.run()
