from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#CREATE DOJOS
@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def index():
    return render_template('dojos.html', all_dojos=Dojo.get_all_dojos())

@app.route('/create/dojo', methods=['Get','POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

#CREATE NINJAS
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', all_dojos=Dojo.get_all_dojos())

@app.route('/create/ninjas', methods=['POST'])
def create_user():
    Ninja.create_ninja(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{dojo_id}')


#READ
@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):
    ninjas = Ninja.get_ninjas_from_dojo(dojo_id)
    return render_template('dojo_ninjas.html', dojo=Dojo.get_dojo(dojo_id), ninjas=ninjas)


# #UPDATE
# @app.route('/ninja/update', methods={'POST'})
# def update(ninja_id):
#     Ninja.update_ninja(request.form)
#     return redirect('/')

# @app.route('/dojos/<int:dojo_id>/update', methods={'POST'})
# def update(dojo_id):
#     Dojo.update_dajo()
#     return redirect('/')


# #DELETE
# @app.route('/dojos/<int:dojo_id>/delete', methods=['POST'])
# def delete(dojo_id):
#     Dojo.delete_dojo(dojo_id)
#     return redirect('/dojos')
