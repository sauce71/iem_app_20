from datetime import date, datetime
from random import randint
from flask import Flask, render_template, request, redirect, url_for
from . import app
from .form import MyForm, MeasurementForm
from .db import add_measurement, select_measurements

@app.route("/")
def index():
    measurements = select_measurements()
    return render_template("index.html", measurements=measurements)


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



@app.route("/measurement/new", methods=['POST', 'GET'])
def measurement_new():
    form = MeasurementForm()
    # message kommer som et url argument når vi har lagret og redirigert
    message = request.args.get('message', None)
    if form.validate_on_submit():
        new_id = add_measurement(
            form.unit_id.data,
            form.registered.data,
            form.bmp280_temperature.data,
            form.bmp280_pressure.data,
            form.si7021_temperature.data,
            form.si7021_humidity.data,
            form.ccs811_tvoc.data,
            form.sds011_dust.data,
        )
        message = 'Ny måling lagret med id {}'.format(new_id)
        # Ved å redirigere til seg selv så får vi nye tilfeldige verdier
        return redirect(url_for('measurement_new', message=message))
    else:
        if not form.errors:
            # Lager nye tilfeldige verdier
            form.registered.data = datetime.now()
            form.bmp280_temperature.data=randint(20,30)
            form.bmp280_pressure.data=randint(950, 1100)
            form.si7021_temperature.data=randint(950, 1100)
            form.si7021_humidity.data=randint(950, 1100)
            form.ccs811_tvoc.data=randint(950, 1100)
            form.sds011_dust.data=randint(950, 1100)
                
    return render_template('measurement_new.html', form=form, message=message)
