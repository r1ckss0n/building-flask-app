import sqlite3

with sqlite3.connect("sample.db") as connection:
   
    c = connection.cursor()
 
    c.execute('DROP TABLE posts')
    c.execute('CREATE TABLE posts(title TEXT, description TEXT)')
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")') 

# to test, run the command python (filename.py in this case sql.py), if it does not return any error
# message, enter the database through the sqlite3 terminal with the command sqlite3 (name of the db.db 
# in this case sample. db)