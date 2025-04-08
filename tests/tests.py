"""module to test the print_version function"""
import unittest
from src.main import print_version


class TestPrintVersion(unittest.TestCase):
    """Test class for print_version function"""
    def test_print_version(self):
        """Test the function with a specific version"""
        actual = print_version()
        expected = "v0.0.2"
        self.assertEqual(actual, expected)
