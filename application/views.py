from datetime import date
from flask import Flask, render_template, request
from . import app
from .form import MyForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template('form.html', dato=date.today())

@app.route("/form/post", methods=['POST'])
def form_post():
    return render_template('form_post.html', 
        firstname=request.form['firstname'],
        lastname=request.form['lastname'],
        dato=request.form['dato'],
        # Bruker for..get() for å få en "default" verdi der det ikke er noen verdi
        ok=request.form.get('ok'),
    )

@app.route("/wtform", methods=['POST', 'GET'])
def wtform():
    form = MyForm()
    results = {}
    if form.validate_on_submit():
        results['Fornavn'] = form.firstname.data
        results['Etternavn'] = form.lastname.data
        results['Dato'] = '{:%d.%m.%Y}'.format(form.dato.data)
    else:
        results['error'] = 'Dette skjedde noe galt'
                
    return render_template('wtform.html', form=form, results=results)