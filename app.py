# impor the flask class forom the flask module
from flask import Flask, render_template, request, url_for, \
    redirect, session, flash, g
from functools import wraps
import sqlite3

# create the aplication object
app = Flask(__name__)

app.secret_key = "1qazxsw23edcvfr4"
app.database = "sample.db"
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

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    #this test did not work because the () was missing in the print
    #print(cur)
    #print(cur.fetchall())
    # post_dict = {}
    posts = []
    for row in cur.fetchall():
        #post_dict["title"] = row[0]
        #post_dict["description"] = row[1]
        posts.append(dict(title=row[0], description=row[1]))
        #print(posts)

    #posts = [dict(title=row[0], descripition=row[1]) for row in cur.fetchall()]
    # print(posts)
    g.db.close()
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
def connect_db():
    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True)
