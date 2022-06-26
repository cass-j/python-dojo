from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.mytable import MyClass

@app.route('/')             # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

@app.route("/new-route", methods=["POST"])
def new_method():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    MyClass.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/friends')

@app.route("/create", methods=["POST"])
def create_user():
    MyClass.save(request.form)
    userID = User.get_user_id(request.form)
    uid = userID[0]['id']
    return redirect(f'/user/show/{uid}')