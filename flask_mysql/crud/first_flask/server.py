#!/usr/bin/env python3

from operator import methodcaller
from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app  #render_template added
# import the class from friend.py
from friend import Friend
app = Flask(__name__)     # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create-friend", methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/friends')

@app.route("/remove-friend", methods=["GET","POST"])
def remove_friend():
    data = {
        "id": request.form["id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
    }
    Friend.delete_friend(data)
    return redirect("/friends")


@app.route("/friends", methods=["GET","Post"])
def my_friends():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    # print(friends)
    return render_template("friends.html", all_friends=friends)

                                # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode



# def remove():
#     query = "SELECT * FROM users WHERE email = %(email)s;"
#     data = { 'email' : request.form['email'] }
#     result = mysql.query_db(query, data)
#     return redirect("/friends")