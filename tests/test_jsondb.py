from unittest import TestCase
from jsondb import JsonDB

class TestJsonDB(TestCase):

    def setUp(self):
        self.fixture = JsonDB({'a': {'z': 1, 'b': {'c': 2}}})

    def test_getitem(self):

        path = 'a/z'
        self.assertEqual(self.fixture[path], 1)

        path = 'a/b/c'
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

    def test_graft(self):

        fixture = JsonDB()

        data = {'z': 1, 'b': {'c': 2}}
        fixture['a'] = data
        print fixture
        self.assertEqual(fixture['a'], data)
