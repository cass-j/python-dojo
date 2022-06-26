# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class MyClass:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
# CREATE
    @classmethod
    def save(cls, data ):
        query = """INSERT INTO mytable ( first_name , last_name , occupation , created_at, updated_at ) 
        VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db( query, data )

# READ
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM myTable;"""
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('default').query_db(query)
        # Create an empty list to append our instances of friends
        myVariable = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            myVariable.append( cls(friend) )
        return myVariable
# UPDATE
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users 
        SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() 
        WHERE id = %(id)s"""
        return connectToMySQL('users').query_db( query, data)

# DELETE
    @classmethod
    def delete_friend(cls, data):
        query = """DELETE FROM mytable WHERE first_name= %(fname)s AND last_name= %(lname)s AND id = %(id)s"""
        return connectToMySQL('first_flask').query_db( query, data)