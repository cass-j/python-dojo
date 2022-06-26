from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

#Create
@app.route("/user/new")
def new_user():
    return render_template("new-user.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    user_id = User.save(request.form)
    return redirect(f'/user/show/{user_id}')

#Read
@app.route("/")
def home():
    return redirect("/users")

@app.route("/users")
def all_users():
    return render_template("read-all.html", all_users= User.get_all())

@app.route("/user/show/<int:id>")
def user_by_id(id):
    return render_template("user-id.html", user_id=User.get_user_by_id(id))

#Update
@app.route("/user/edit/<int:id>")
def edit_user(id):
    return render_template("edit-user.html", user_id=User.get_user_by_id(id))

@app.route("/update/<int:id>", methods=["POST"])
def update_user(id):
    User.update_user(request.form)
    return redirect(f"/user/show/{id}")

#Delete
@app.route("/user/delete/<int:id>")
def delete_user(id):
    User.delete_user(id)
    return redirect("/users")