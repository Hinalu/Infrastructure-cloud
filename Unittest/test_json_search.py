# Task U1: Lab 3.5.7 - The Unit Test
import unittest
from recursive_json_search import json_search

class JsonSearchTest(unittest.TestCase):
    
    def setUp(self):
        # Sample data to test against
        self.data = {
            "id": "1",
            "name": "DevNet",
            "details": {
                "location": "Brussels",
                "exam": "200-901"
            },
            "hosts": [
                {"hostname": "csr1000v", "ip": "192.168.56.101"}
            ]
        }

    def test_search_found_simple(self):
        """Test finding a key at the top level"""
        self.assertEqual(json_search("name", self.data), "DevNet")

    def test_search_found_nested(self):
        """Test finding a key nested inside a dictionary"""
        self.assertEqual(json_search("location", self.data), "Brussels")

    def test_search_found_list(self):
        """Test finding a key nested inside a list"""
        self.assertEqual(json_search("hostname", self.data), "csr1000v")

    def test_search_not_found(self):
        """Test searching for a key that doesn't exist"""
        self.assertIsNone(json_search("invalid_key", self.data))

if __name__ == '__main__':
    unittest.main()