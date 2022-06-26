# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @staticmethod
    def validate_survey(form):
        is_valid = True
        if len(form['name']) < 3:
            flash('Name must be at least 3 characters.')
            is_valid = False
        if not form['location']:
            flash('Must select a Dojo Location.')
            is_valid = False
        if not form['language']:
            flash('Must select a Dojo Location.')
            is_valid = False
        if len(form['comment']) < 3:
            flash('Comments must be at least 3 characters.')
            is_valid = False
        return is_valid

#Create
    @classmethod
    def save_survey(cls, data):
        query = """INSERT INTO dojos ( name , location , language , comment , created_at, updated_at ) 
        VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey').query_db( query, data)

#Read
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL('dojo_survey').query_db(query)
        myVariable = []
        for user in results:
            myVariable.append( cls(user) )
        return myVariable

    @classmethod
    def get_survey(cls, data):
        id = {
        "id" : data
        }
        query = """SELECT * FROM dojos WHERE id = %(id)s"""
        return connectToMySQL('dojo_survey').query_db(query, id)

#Update
    @classmethod
    def update_survey(cls, data):
        query = """UPDATE dojos 
        SET name = %(name)s, location = %(location)s, language = %(language)s, updated_at = NOW() 
        WHERE id = %(id)s"""
        return connectToMySQL('dojo_survey').query_db( query, data)

#Delete
    @classmethod
    def delete_survey(cls, data):
        id = {
        "id" : data
        }
        query = """DELETE FROM dojos WHERE id = %(id)s"""
        return connectToMySQL('dojo_survey').query_db( query, id)