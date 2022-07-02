from genericpath import exists
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
import re
from flask_app.models.user import User
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/create/user", methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')

    session['id'] = User.create_user(request.form)
    session['fname'] = request.form.get('fname')
    user_id = session['id']
    session['is_logged_in'] = True
    return redirect(f'/dashboard/{user_id}')

@app.route('/login', methods=['post'])
def validate():
    if not User.validate_login(request.form):
        return redirect('/')
    user_id = User.get_id(request.form)
    if not user_id:
        return redirect('/')
    session['is_logged_in'] = True
    return redirect(f'/dashboard/{user_id}')

@app.route('/dashboard/<user_id>', methods=['GET'])
def dashboard(user_id):
    if not session.get('is_logged_in'):
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Bcrypt args
# bcrypt.generate_password_hash(password_string)
# bcrypt.check_password_hash(hashed_password, password_string)