"""Module to create a Flask API for the application."""

from datetime import datetime, timedelta, timezone
from flask import Flask
import requests
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from src.version import APP_VERSION


app = Flask(__name__)


@app.route('/version')
def version():
    """Return the version of the application."""
    return {'version': f"{APP_VERSION}"}, 200


@app.route('/temperature')
def temperature():
    """Return current average temperature based on all senseBox data."""
    url = "https://api.opensensemap.org/boxes"
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours=1)
    opense_time_format = start.strftime("%Y-%m-%dT%H:%M:%SZ")
    params = {
        'date': opense_time_format,
        'phenomenon': 'temperature',
    }
    response = requests.get(url, params=params, timeout=20).json()
    temperatures = []
    for location in response:
        for sensors in location.get('sensors', []):
            title = sensors.get('title').lower()
            if "temp" in title:
                temp = sensors.get('lastMeasurement', {}).get('value')
                if temp is not None:
                    temperatures.append(temp)
    average_temp = get_average_temp(temperatures)
    server_response = {
        'average_temperature': average_temp,
        'unit': '°C',
        'timestamp': now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    return server_response, 200


def get_average_temp(temperatures):
    """Return the average temperature."""
    if len(temperatures) == 0:
        return 0
    return sum(map(float, temperatures)) / len(temperatures)


@app.route('/metrics')
def metrics():
    """Return the metrics of the application."""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    app.run(debug=True)
