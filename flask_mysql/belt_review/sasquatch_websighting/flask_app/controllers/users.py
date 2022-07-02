from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
import re
from flask_app.models.user import Users
from flask_app.models.sighting import Sightings
bcrypt=Bcrypt(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title = '404'), 404


@app.route('/')
def index():
    return render_template('index.html')


# CREATE
@app.route("/register", methods=["POST"])
def register_user():
    if not Users.validate_user(request.form):
        return redirect('/')
    session['id'] = Users.register(request.form)
    if not session.get('id'):
        flash('Registration Failed')
        return redirect('/')
    session['logged_in'] = True
    return redirect(f'/dashboard')

@app.route('/new/sighting')
def create_post():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('sighting_new.html', user_info=Users.get_user_by_id(session['id']))

@app.route('/post_sighting', methods=['POST'])
def post_sighting():
    if not Sightings.validate_post(request.form):
        return redirect('/new/sighting')
    Sightings.create_post(request.form)
    return redirect('/dashboard')


# READ
@app.route('/login', methods=['POST'])
def login():
    if not Users.validate_login(request.form):
        return redirect('/')
    session['id'] = Users.get_user_by_email(request.form)
    session['logged_in'] = True
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('dashboard.html', user_info=Users.get_user_by_id(session['id']), posts=Sightings.get_sightings())

@app.route('/show/<int:post_id>')
def show_post(post_id):
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('sighting_show.html', user_info=Users.get_user_by_id(session['id']), posts=Sightings.get_sighting_details(post_id))


# UPDATE
@app.route('/update/<int:post_id>', methods=['POST'])
def update_post(post_id):
    if not Sightings.validate_post:
        redirect('/dashboard')
    Sightings.update_sighting(request.form, post_id)
    return redirect('/dashboard')

@app.route('/edit/<int:post_id>', methods=['GET','POST'])
def edit_post(post_id):
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('sighting_edit.html', user_info=Users.get_user_by_id(session['id']), posts=Sightings.get_one_sighting(post_id))


# Delete
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/delete/<int:post_id>', methods=['POST'])
def shred(post_id):
    Sightings.delete_post(post_id)
    return redirect('/dashboard')