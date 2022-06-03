#!/usr/bin/env python3

from flask import Flask, render_template   # Import Flask to allow us to create our app  #render_template added
app = Flask(__name__)       # Create a new instance of the Flask class called "app"

@app.route('/')             # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

                                # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode