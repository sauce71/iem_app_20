from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class MyForm(FlaskForm):
    firstname = StringField('Fornavn', validators=[DataRequired()], default='Tom Øyvind')
    lastname = StringField('Etternavn', validators=[DataRequired()], default='Hogstad')
    dato = DateField('Dato', default=date.today())
