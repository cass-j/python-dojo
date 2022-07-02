# import the function that will return an instance of a connection
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re
bcrypt=Bcrypt(app)

class Sightings:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.date = data['date']
        self.number_sighted = data['number_sighted']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_post( post ):
        is_valid = True
        if len(post['location']) < 3:
            flash('Location name must be 3 or more letters.')
            is_valid = False
        if len(post['number']) < 1:
            flash('Must report at least 1 sasquatch.')
            is_valid = False
        if not len(post['description']) > 3:
            flash('Explain what happened.')
            is_valid = False
        if not len(post['date']) == 10:
            flash('Enter a valid date!')
            is_valid = False
        return is_valid

# CREATE
    @classmethod
    def create_post(cls, data ):
        query = """INSERT INTO sightings 
        ( location , date , number_sighted , description , users_id , created_at, updated_at ) 
        VALUES ( %(location)s , %(date)s , %(number)s , %(description)s , %(users_id)s , NOW() , NOW() );"""
        return connectToMySQL('sasquatch_web').query_db( query, data )

# READ
    @classmethod
    def get_one_sighting(cls, data):
        data = {
            'id' : data
        }
        query = """SELECT * FROM sightings WHERE id = %(id)s;"""
        return connectToMySQL('sasquatch_web').query_db(query, data)

    @classmethod
    def get_sightings(cls):
        query = """SELECT sightings.id AS 'sid', sightings.location, sightings.date, users.id, users.first_name, users.last_name  
                FROM users
                JOIN sightings ON users.id = sightings.users_id
                ORDER BY sightings.id ASC;"""
        results = connectToMySQL('sasquatch_web').query_db(query)
        return results

    @classmethod
    def get_sighting_details(cls, data):
        data = {
            'id' : data
        }
        query = """SELECT sightings.id AS 'sid', sightings.location, sightings.date, sightings.description, sightings.number_sighted, users.id, users.first_name, users.last_name
                FROM users
                JOIN sightings ON users.id = sightings.users_id
                WHERE sightings.id = %(id)s;"""
        return connectToMySQL('sasquatch_web').query_db(query, data)

# UPDATE
    @classmethod
    def update_sighting(cls, data, post_id):
        data = {
            'id' : post_id,
            'location' : data['location'],
            'date' : data['date'],
            'number' : data['number'],
            'description' : data['description']
        }
        query = """UPDATE sightings
        SET location = %(location)s, date = %(date)s, number_sighted = %(number)s, description = %(description)s, updated_at = NOW() 
        WHERE id = %(id)s"""
        return connectToMySQL('sasquatch_web').query_db( query, data)

# DELETE
    @classmethod
    def delete_post(cls, data):
        data = {
            "id" : data
        }
        query = """DELETE FROM sightings
        WHERE id = %(id)s"""
        return connectToMySQL('sasquatch_web').query_db( query, data)