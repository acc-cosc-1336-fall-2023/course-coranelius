import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    
    def test_get_options_ratio_1(self):
        ratio = get_options_ratio(5,20)
        self.assertEqual(ratio, 0.25)
    
    def test_get_options_ratio_2(self):
        ratio = get_options_ratio(10, 20)
        self.assertEqual(ratio, .5)

class Test_Config(unittest.TestCase):
    def get_faculty_rating_1(self):
        self.assertEqual(get_faculty_rating(.91),"Excellent")
        self.assertEqual(get_faculty_rating(.85),"Very Good")
        self.assertEqual(get_faculty_rating(.71),"Good")
        self.assertEqual(get_faculty_rating(.66),"Needs Improvement")
        self.assertEqual(get_faculty_rating(.45),"Unacceptable")

import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):

    def test_factorial_4(self):
        self.assertEqual(get_factorial(4), 24)

    def test_factorial_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_factorial_6(self):
        self.assertEqual(get_factorial(4), 720)

    def test_sum_odd_7(self):
        self.assertEqual(sum_odd_numbers(7), 16)

    def test_sum_odd_9(self):
        self.assertEqual(sum_odd_numbers(9), 25)

    def test_sum_odd_10(self):
        self.assertEqual(sum_odd_numbers(7), 25)