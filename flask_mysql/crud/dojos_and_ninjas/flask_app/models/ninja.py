# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

# CREATE
    @classmethod
    def create_ninja(cls, data):
        query = """INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id )
        VALUES ( %(fname)s , %(lname)s , %(age)s , NOW() , NOW() , %(dojo_id)s );"""
        return connectToMySQL('dojos_and_ninjas').query_db( query, data)

# READ
    @classmethod
    def get_ninjas_from_dojo(cls, data):
        data = {
            'dojo_id' : data
        }
        query = """SELECT * FROM ninjas where dojo_id = %(dojo_id)s;"""
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

# # UPDATE
#     @classmethod
#     def update_ninja(cls, data):
#         query = """UPDATE ninjas 
#         SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, dojo_id = %(dojo)s, updated_at = NOW() 
#         WHERE id = %(id)s"""
#         return connectToMySQL('dojos_and_ninjas').query_db( query, data)

# # DELETE
#     @classmethod
#     def delete_ninja(cls, data):
#         data = {
#             'id' : data
#         }
#         query = """DELETE FROM mytable WHERE id = %(id)s"""
#         return connectToMySQL('dojos_and_ninjas').query_db( query, data)