from datetime import date
from flask import Flask, render_template, request
from . import app

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
