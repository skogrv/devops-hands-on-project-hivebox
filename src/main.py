"""Module providing featching data from OpenSense API"""
import requests
from datetime import datetime, timedelta, timezone
APP_VERSION = '0.0.2'


def print_version():
    """Function printing app version"""
    return f"{APP_VERSION}"


def get_opensense_data():
    """Function to get OpenSense data"""
    url = "https://api.opensensemap.org/boxes"
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours = 1)
    opense_time_format = start.strftime("%Y-%m-%dT%H:%M:%SZ")
    params = {
        'date': opense_time_format,
        'limit': 1,        
        'phenomenon': 'temperature',
    }
    response = requests.get(url, params=params).json()
    print(response)


if __name__ == '__main__':
    print_version()
    get_opensense_data()
