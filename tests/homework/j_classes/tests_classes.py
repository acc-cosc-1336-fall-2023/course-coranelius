import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_get_rolled_value(self):
        die_instance = Die()

        for _ in range(3):  
            die_instance.roll()
            rolled_value = die_instance.get_rolled_value()
            self.assertTrue(1 <= rolled_value <= 6, f"Invalid value that was rolled: {rolled_value}")