from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    if not Survey.validate_survey(request.form):
        return redirect('/')

    session['name'] = request.form.get('name')
    session['location'] = request.form.get('location')
    session['language'] = request.form.get('language')
    session['comment'] = request.form.get('comment')
    
    Survey.save_survey(request.form)
    return redirect('/results')

@app.route('/results', methods=['GET'])
def results():
        return render_template('results.html',)

                                # app.run(debug=True) should be the very last statement!
if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode