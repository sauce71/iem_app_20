from datetime import date
from flask import Flask, render_template, request, current_app, g
from . import app
from .db import add_measurement

@app.route('/api/post_data', methods=('POST',))
def api_post_data():
    """
    Start på api for å motta data fra ESP
    Data sendes som json
    """
    # Bygger inn litt sikkerhet. Api kallet vårt må identifisere seg med en nøkkel.
    #if request.headers.get('X-api-key') == current_app.config['API_KEY']:
    data = request.json
    # TODO: Utvid med feltene til sensorene deres
    add_measurement(
        data['unit_id'],
        data['registered'],
        data['bmp280_temperature'],
        data['bmp280_pressure'],
        data['si7021_temperature'],
        data['si7021_humidity'],
        data['ccs811_tvoc'],
        data['sds011_dust']
    )
    print('Data i Flask App:', data)
    #else:
        # Hvis ikke rikitg nøkkel, så returnere vi en 401 kode: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
    #    abort(401)
    return 'Data received!'

