import os
from flask import Flask, send_from_directory


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    # load the instance config, if it exists
    #app.config.from_pyfile("config.py", silent=False)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #piapp.add_url_rule("/", endpoint="index")

    @app.route('/favicon.ico')
    def favicon():
        """
        Netllesere ber alltd om favicon i tilegg til siden
        Favicon kan du lage her: https://realfavicongenerator.net
        """
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app

app = create_app()

from . import views 