import json

from datetime import date
from unittest import TestCase


class TestData(TestCase):
    @classmethod
    def setUpClass(cls):
        with open("dates.json", "r") as f:
            cls.data = json.load(f)


class TestDataStructure(TestData):
    def test_classes(self):
        for k in ["valid", "invalid", "extra", "examples"]:
            self.assertIn(k, self.data)

    def test_year_data(self):
        for k in ["valid", "invalid", "extra", "examples"]:
            for d in self.data[k]:
                for f in [
                    "year", "month", "day",
                    "calendar", "description", "comment"
                ]:
                    self.assertIn(f, d)


class TestDataConsistency(TestData):
    def test_classes(self):
        s = set()
        for k in ["valid", "invalid", "extra", "examples"]:
            for d in self.data[k]:
                self.assertNotIn(d["description"], s)
                s.add(d["description"])


class TestValidDates(TestData):
    def test_valid_dates_are_valid(self):
        for d in self.data["valid"]:
            dobj = date(d["year"], d["month"], d["day"])
            self.assertIsNotNone(dobj)

    def test_example_dates_are_valid(self):
        for d in self.data["examples"]:
            dobj = date(d["year"], d["month"], d["day"])
            self.assertIsNotNone(dobj)
