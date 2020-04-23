"""
Database funksjonalitet
Se tutorial:
https://flask.palletsprojects.com/en/1.1.x/tutorial/database/

Python:
https://docs.python.org/3.8/library/sqlite3.html

SQLite:
https://www.sqlite.org/index.html
"""
import os
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Denne funksjonen åpner databasen som den henter fra instance/config.py
    Den lager tilkoblingen i g (Globale variabler i flask) for at en ikke skal lage en ny tilkobling
    hver gang en kaller get_db()
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            os.path.join(current_app.instance_path, current_app.config['DATABASE']),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)


def init_db():
    db = get_db()
    with current_app.open_resource('data/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def add_measurement(unit_id, registered, bmp280_temperature, bmp280_pressure, si7021_temperature, si7021_humidity, ccs811_tvoc, sds011_dust):
    '''
    Legger til en post i tabellen med målinge
    '''
    db = get_db() 
    c = db.cursor()
    # Vi skriver inn SQL koden i en string som kan gå over flere linjer
    # Vi bruker parameter for å unngå SQL injection hacks
    c.execute('''
        INSERT INTO measurement(unit_id, registered, bmp280_temperature, bmp280_pressure, si7021_temperature, si7021_humidity, ccs811_tvoc, sds011_dust)
        VALUES (?,?,?,?,?,?,?,?)
        ''', 
        (unit_id, registered, bmp280_temperature, bmp280_pressure, si7021_temperature, si7021_humidity, ccs811_tvoc, sds011_dust) # tuple eller liste, () eller []
        )
    db.commit()
    return c.lastrowid

def select_measurements():
    db = get_db()
    c = db.cursor()
    c.execute('''
        SELECT * FROM measurement ORDER BY registered DESC
        '''
        )
    return c.fetchall()

