from flask import Flask   # Import Flask to allow us to create our app  #render_template added
app = Flask(__name__)     # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'