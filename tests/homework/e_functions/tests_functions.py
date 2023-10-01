import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds


class Test_Config(unittest.TestCase):
    def test_get_hour(self):
        result_hour = get_hour(3800)
        self.assertEqual(result_hour, 1)

        result_hour2 = get_hour(3600)
        self.assertEqual(result_hour2, 1)

    def test_get_minutes(self):
        result_minutes = get_minutes(3800)
        self.assertEqual(result_minutes, 3)

        result_minutes = get_minutes(3600)
        self.assertEqual(result_minutes, 0)

    def test_get_seconds(self):
        result_seconds = get_seconds(3800)
        self.assertEqual(result_seconds, 20)
        
        result_seconds = get_seconds(3600)
        self.assertEqual(result_seconds, 0)
        