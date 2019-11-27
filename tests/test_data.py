import json

from unittest import TestCase


class TestData(TestCase):
    @classmethod
    def setUpClass(cls):
        with open("dates.json", "r") as f:
            cls.data = json.load(f)
    
    def test_classes(self):
        for k in ["valid", "invalid", "extra", "examples"]:
            self.assertIn(k, self.data)
