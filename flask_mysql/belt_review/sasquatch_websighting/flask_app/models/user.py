# import the function that will return an instance of a connection
import string
import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import sighting
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt=Bcrypt(app)

class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user( user ):
        is_valid = True
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        results = connectToMySQL('sasquatch_web').query_db(query, user)
        if len(results) > 1:
            flash("Email already in use.")
            is_valid=False
        if len(user['email']) < 1:
            flash('Enter an email!')
            return False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not len(user['fname']) > 1:
            flash('First name must be at least 3 characters.')
            is_valid = False
        if not len(user['lname']) > 1:
            flash('Last name must be at least 3 characters.')
            is_valid = False
        if not len(user['pword']) > 7:
            flash('Password must be at least 8 characters.')
            is_valid = False
        if not user['pword'] == user['confirm_pword']:
            flash('Passwords must match')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login( user ):
        is_valid = True
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        results = connectToMySQL('sasquatch_web').query_db(query, user)
        if len(user['email']) < 1:
            flash('Enter an email!')
            return False
        if len(user['pword']) < 1:
            flash('Enter a password!')
            return False
        if results == ():
            flash('Invalid email / password!')
            return False
        if len(user['pword']) < 7 or len(user['email']) < 5 or not EMAIL_REGEX.match(user['email']):
            flash('Invalid email / password!')
            is_valid = False
        if not bcrypt.check_password_hash(results[0]['password'], user['pword']):
            flash('Invalid email / password!')
            is_valid = False
        return is_valid

# CREATE
    @classmethod
    def register(cls, data ):
        user_info = {
            "fname" : data['fname'],
            "lname" : data['lname'],
            "email" : data['email'],
            "pword" : bcrypt.generate_password_hash(data['pword']),
        }
        query = """INSERT INTO users 
        ( first_name , last_name , email , password , created_at, updated_at ) 
        VALUES ( %(fname)s , %(lname)s , %(email)s , %(pword)s , NOW() , NOW() );"""
        return connectToMySQL('sasquatch_web').query_db( query, user_info )

# READ
    @classmethod
    def get_user_by_id(cls, data):
        data = {
            'id' : data
        }
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        results = connectToMySQL('sasquatch_web').query_db(query, data)
        myVariable = []
        for item in results:
            myVariable.append( cls(item) )
        return myVariable

    @classmethod
    def get_user_by_email(cls, data):
        query = """SELECT * FROM users WHERE email = %(email)s"""
        results = connectToMySQL('sasquatch_web').query_db(query, data)
        if len(results) < 1:
            return False
        return results[0]['id']

# UPDATE
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users
        SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, password = %(pword)s updated_at = NOW() 
        WHERE id = %(id)s"""
        return connectToMySQL('sasquatch_web').query_db( query, data)

# DELETE
    @classmethod
    def delete_user(cls, data):
        query = """DELETE FROM sightings WHERE id = %(id)s"""
        return connectToMySQL('sasquatch_web').query_db( query, data)