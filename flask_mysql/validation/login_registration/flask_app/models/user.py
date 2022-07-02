# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.birthdate =data['birthdate']
        self.language = data['language']
        self.last_login = data['last_login']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user( user ):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_register').query_db(query, user)
        if len(results) >= 1:
            flash("Email already in use.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not len(user['fname']) > 2:
            flash('First name must be at least 3 characters.')
            is_valid = False
        if not len(user['lname']) > 2:
            flash('Last name must be at least 3 characters.')
            is_valid = False
        if not len(user['password']) > 2:
            flash('Password must be at least 3 characters.')
            is_valid = False
        if not user['password'] == user['confirm_pass']:
            flash('Passwords must match')
            is_valid = False
        if not user['birthdate']:
            flash('Must enter a Birth Date.')
            is_valid = False
        if not user['language']:
            flash('Must select a Favorite Language.')
            is_valid = False
        return is_valid

    @classmethod
    def validate_login(cls, user):
        is_valid = True
        query = """Select * FROM users where email = %(email)s;"""
        results = connectToMySQL('login_register').query_db(query, user)
        if len(user['password']) < 3 or len(user['email']) < 5 or not EMAIL_REGEX.match(user['email']):
            flash("Invalid email / password!")
            is_valid = False
        if len(results) < 1:
            return False
        if not bcrypt.check_password_hash(results[0]['password'], user['password']):
            flash('Invalid email / password!')
            is_valid = False
        return is_valid


# CREATE
    @classmethod
    def create_user(cls, data ):
        data = {
            "fname" : str.title(data['fname']),
            "lname" : str.title(data['lname']),
            "email" : str.lower(data['email']),
            "password" : bcrypt.generate_password_hash(data['password']),
            "birthdate" : data['birthdate'],
            "language" : data['language']
        }
        query = """INSERT INTO users
        ( first_name , last_name , email , password , birthdate , language , last_login , created_at, updated_at ) 
        VALUES ( %(fname)s , %(lname)s , %(email)s , %(password)s , %(birthdate)s , %(language)s , NOW() , NOW() , NOW() );"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('login_register').query_db( query, data )

# READ
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users;"""
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_register').query_db(query)
        # Create an empty list to append our instances of friends
        myVariable = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            myVariable.append( cls(user) )
        return myVariable

    @classmethod
    def get_id(cls, data):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        results = connectToMySQL('login_register').query_db(query, data)
        if len(results) < 1:
            return False
        return results[0]['id']

