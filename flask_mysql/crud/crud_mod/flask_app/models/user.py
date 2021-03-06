# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
#Create
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) 
        VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data)

#Read
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users;"""
        results = connectToMySQL('users').query_db(query)
        myVariable = []
        for user in results:
            myVariable.append( cls(user) )
        return myVariable

    @classmethod
    def get_user_by_id(cls, data):
        id = {
        "id" : data
        }
        query = """SELECT * FROM users WHERE id = %(id)s"""
        return connectToMySQL('users').query_db(query, id)
    
    @classmethod
    def get_user_id(cls, data):
        query = """SELECT id FROM users WHERE first_name = %(fname)s AND last_name = %(lname)s AND email = %(email)s"""
        return connectToMySQL('users').query_db(query,data)

#Update
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users 
        SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() 
        WHERE id = %(id)s"""
        return connectToMySQL('users').query_db( query, data)

#Delete
    @classmethod
    def delete_user(cls, data):
        id = {
        "id" : data
        }
        query = """DELETE FROM users WHERE id = %(id)s"""
        return connectToMySQL('users').query_db( query, id)


    # @classmethod
    # def verify_email(cls, data):
    #     query = """select email from users where email = %(email)s"""
    #     return connectToMySQL('users').query_db( query, data)