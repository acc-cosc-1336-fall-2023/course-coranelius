import unittest

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

class TestSetOperations(unittest.TestCase):
    def test_intersection(self):
        result = baseball.intersection(basketball)
        self.assertEqual(result, {'Carmen', 'Alicia'})

    def test_union(self):
        result = baseball.union(basketball)
        self.assertEqual(result, {'Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah'})

    def test_difference_baseball(self):
        result = baseball.difference(basketball)
        self.assertEqual(result, {'Jodi', 'Aida'})

    def test_difference_basketball(self):
        result = basketball.difference(baseball)
        self.assertEqual(result, {'Eva', 'Sarah'})

    def test_symmetric_difference(self):
        result = baseball.symmetric_difference(basketball)
        self.assertEqual(result, {'Jodi', 'Aida', 'Eva', 'Sarah'})