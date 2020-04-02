from random import randint
from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, DateTimeField


class MyForm(FlaskForm):
    firstname = StringField('Fornavn', validators=[DataRequired()], render_kw={"placeholder": "Ditt fornavn"})
    lastname = StringField('Etternavn', validators=[DataRequired()], default='Hogstad')
    dato = DateField('Dato', default=date.today())


class MeasurementForm(FlaskForm):
    unit_id = IntegerField('Enhet', default=1, validators=[DataRequired()])
    registered = DateTimeField('Dato/Tid', default=datetime.now(), validators=[DataRequired()])
    bmp280_temperature = FloatField('BME280 Temperatur', validators=[DataRequired()])
    bmp280_pressure = FloatField('BME280 Trykk', validators=[DataRequired()])
