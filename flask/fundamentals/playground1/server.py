#!/usr/bin/env python3

from flask import Flask, render_template   # Import Flask to allow us to create our app  #render_template added
app = Flask(__name__)       # Create a new instance of the Flask class called "app"

@app.route('/')             # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('index.html', default=3)

@app.route('/play/<int:x>')
def replay(x):
    if x > 4:
        row = int(x/4)
        fill = int(x % 4)
    else:
        row = 1
        fill = x
    return render_template('index.html', boxes=x, rows=row, last=fill)

@app.route('/play/<int:x>/<string:colors>')

def rereplay(x, colors):
    if x > 4:
        row = int(x/4)
        fill = int(x % 4)
    else:
        row = 1
        fill = x
    return render_template('index.html', boxes=x, rows=row, last=fill, color=colors)

                            # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode