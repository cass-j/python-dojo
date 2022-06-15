#!/usr/bin/env python3

from flask import Flask, render_template   # Import Flask to allow us to create our app  #render_template added
app = Flask(__name__)       # Create a new instance of the Flask class called "app"

@app.route('/')             # The "@" decorator associates this route with the function immediately following
def index():
    string = 'Checker'
    length = len(string)
    return render_template('index.html', string=string, length=length)

# @app.route('/')
# def index():
#     return"yay!!!"

@app.route('/<int:y>')
def wide(y):
    string = 'Checkerboard'
    length = len(string)
    return render_template('index.html', columns=8, rows=y, string=string, length=length)


@app.route('/<int:y>/<int:x>')
def sizable(y,x):
    string = str.title('Checker board')
    length = len(string)
    return render_template('index.html', columns=x, rows=y, string=string, length=length)


@app.route('/<int:y>/<int:x>/<color1>/<color2>')
def colorize(y,x,color1,color2):
    string = str.title('Checker board!')
    length = len(string)
    color1 = color1
    color2 = color2
    return render_template('index.html', columns=x, rows=y, string=string, length=length, c1=color1, c2=color2)


                                # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode