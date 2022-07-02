from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
import re
from flask_app.models import user
from flask_app.models.sighting import Sightings
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/new-route", methods=["POST"])
def new_method():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ" : request.form["occ"]
    }
    Users.save(data)
    return redirect('/friends')

@app.route("/create", methods=["POST"])
def create_user():
    Users.save(request.form)
    userID = Users.get_user_id(request.form)
    uid = userID[0]['id']
    return redirect(f'/user/show/{uid}')