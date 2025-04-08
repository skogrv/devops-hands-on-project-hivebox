from flask import Flask
from src.main import APP_VERSION


app = Flask(__name__)

@app.route('/version')
def version():
    """Return the version of the application."""
    return {'version': f"{APP_VERSION}"}, 200