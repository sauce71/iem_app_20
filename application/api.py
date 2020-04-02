from datetime import date
from flask import Flask, render_template, request, current_app, g
from . import app

@app.route('/api/post_data', methods=('POST',))
def api_post_data():
    """
    Start på api for å motta data fra ESP
    Data sendes som json
    """
    # Bygger inn litt sikkerhet. Api kallet vårt må identifisere seg med en nøkkel.
    if request.headers.get('X-api-key') == current_app.config['API_KEY']:
        data = request.json()
        print(data)
    else:
        # Hvis ikke rikitg nøkkel, så returnere vi en 401 kode: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
        abort(401)
    return 'Data received!'

