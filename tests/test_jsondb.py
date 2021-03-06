import json
from unittest import TestCase
from jsondb import JsonDB

class TestJsonDB(TestCase):

    def setUp(self):
        self.fixture = JsonDB({'a': {'z': 1, 'b': {'c': 2}}})

    def test_getitem(self):

        path = 'a/z'
        self.assertEqual(self.fixture[path], 1)

        path = 'a/b/c/'
        self.assertEqual(self.fixture[path], 2)

        path = 'a/b'
        self.assertEqual(self.fixture[path], {'c': 2})

        """
        with self.assertRaises(KeyError):
            self.fixture['b/o/g/u/s']
        """

        self.assertRaises(KeyError, self.fixture.__getitem__,
                          'b/o/g/u/s')

    def test_setitem(self):
        
        path = 'a/z'
        self.fixture[path] = 2
        self.assertEqual(self.fixture[path], 2)

    def test_delitem(self):
        path = 'a/z'
        del self.fixture[path]
        self.assertEqual(self.fixture, {'a': {'b': {'c': 2}}})

    def test_graft(self):

        fixture = JsonDB()

        data = {'z': 1, 'b': {'c': 2}}
        fixture['a'] = data
        self.assertEqual(fixture['a'], data)

    def test_json(self):
        self.assertTrue(len(json.dumps(self.fixture)) > 0)

    def test_contains(self):

        self.assertTrue('a/z' in self.fixture)
        self.assertTrue('a/b/c' in self.fixture)
