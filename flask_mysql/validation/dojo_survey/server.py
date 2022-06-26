#!/usr/bin/env python3
from flask_app.controllers import surveys
from flask_app import app
from operator import methodcaller

                                # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode