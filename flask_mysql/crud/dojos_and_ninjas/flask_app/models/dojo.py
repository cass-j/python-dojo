# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CREATE
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"""
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

# READ
    @classmethod
    def get_all_dojos(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        data = []
        for ninja in results:
            data.append( cls(ninja) )
        return data

    @classmethod
    def get_dojo(cls,data):
        data = {
            'id' : data
        }
        query = """Select * FROM dojos WHERE id = %(id)s"""
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

# # UPDATE
#     @classmethod
#     def update_dojo(cls, data):
#         query = """UPDATE dojos
#         SET name = %(name)s, updated_at = NOW()
#         WHERE id = %(id)s"""
#         return connectToMySQL('dojos_and_ninjas').query_db( query, data)

# # DELETE
#     @classmethod
#     def delete_dojo(cls, data):
#         data = {
#             'id': data
#         }
#         query = """DELETE FROM dojos WHERE id = %(id)s"""
#         return connectToMySQL('dojos_and_ninjas').query_db( query, data)