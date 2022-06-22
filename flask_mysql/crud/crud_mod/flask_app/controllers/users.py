from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

#Create
@app.route("/user/new")
def new_user():
    return render_template("new-user.html")

@app.route("/create", methods=["POST"])
def create_user():
    User.save(request.form)
    userID = User.get_user_id(request.form)
    uid = userID[0]['id']
    return redirect(f'/user/show/{uid}')

#Read
@app.route("/")
def home():
    redirect("/users")

@app.route("/users")
def all_users():
    return render_template("read-all.html", all_users= User.get_all())

@app.route("/user/show/<int:id>")
def user_by_id(id):
    data = {
        "id" : id
    }
    return render_template("user-id.html", id=id, query=User.get_user_by_id(data))

#Update
@app.route("/user/edit/<int:id>")
def edit_user(id):
    data = {
        "id" : id
    }
    return render_template("edit-user.html", id=id, query=User.get_user_by_id(data))

@app.route("/update/<int:id>", methods=["POST"])
def update_user(id):
    User.update_user(request.form)
    return redirect(f"/user/show/{id}")

#Delete
@app.route("/user/delete/<int:id>")
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete_user(data)
    return redirect("/users")