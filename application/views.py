from flask import Flask, render_template, request
from . import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/form/post", methods=['POST'])
def form_post():
    return '<pre>Fornavn: {}\nEtternavn: {}\nDato:{}</pre>'.format(
        request.form['firstname'], 
        request.form['lastname'], 
        request.form['dato'])
