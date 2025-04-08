"""Module to provide unit testing functions"""
import unittest
import requests
from src.main import print_version


class TestPrintVersion(unittest.TestCase):
    """Test class for print_version function"""
    def test_print_version(self):
        """Test the function with a specific version"""
        url = 'http://127.0.0.1:5000/version'
        actual = requests.get(url, timeout=5).json().get('version')
        print(actual)
        expected = print_version()
        self.assertEqual(actual, expected)