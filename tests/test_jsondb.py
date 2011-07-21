from unittest import TestCase
from jsondb import JsonDB

class TestJsonDB(TestCase):

    def test_from_path(self):
        fixture = JsonDB()
        fixture['a'] = {'z': 1, 'b': {'c': 2}}

        path = 'a/z'
        self.assertEqual(fixture.from_path(path), 1)

        path = 'a/b/c'
        self.assertEqual(fixture.from_path(path), 2)

        path = 'a/b'
        self.assertEqual(fixture.from_path(path), {'c': 2})
