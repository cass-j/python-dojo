#!/usr/bin/env python3

from flask import Flask, render_template     # Import Flask to allow us to create our app  #render_template added
app = Flask(__name__)       # Create a new instance of the Flask class called "app"

@app.route('/')             # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', phrase='hello', times=5)
    # return 'Hello World!'   # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return 'Success!'

@app.route('/hello/<name>')
def name(name):
        return (f'Hello {str.title(name)}') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'

@app.route('/users/<username>/<id>')    # for a route '/users/____/____', two parameters in the url get passed as username and id
def profileInfo(username, id):
    print(username)
    print(id)
    return (f'username: {username}, id: {id}')

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


                            # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode.