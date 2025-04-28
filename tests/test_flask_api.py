"""Module to provide unit testing functions"""
import unittest
import requests
from src.version import APP_VERSION


class TestPrintVersion(unittest.TestCase):
    """Test class for print_version function"""

    def test_print_version(self):
        """Test the function with a specific version"""
        correct_version = APP_VERSION
        url = 'http://127.0.0.1:5000/version'
        response = requests.get(url, timeout=5)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get('version'), correct_version)



class TemperatureEndpointTest(unittest.TestCase):
    """"Test class for temperature endpoint"""

    def test_temperature(self):
        """Test the temperature endpoint"""
        url = 'http://127.0.0.1:5000/temperature'
        response = requests.get(url, timeout=20)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, float)
