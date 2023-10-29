import unittest
from src.homework.i_dictionaries_sets.dictionary import Inventory


class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        my_inventory = Inventory()


        my_inventory.add_inventory("Widget1", 10)
        self.assertEqual(my_inventory.items["Widget1"], 10, "Widget1 test 1 failed.")

        my_inventory.add_inventory("Widget1", 25)
        self.assertEqual(my_inventory.items["Widget1"], 35, "Widget1 test 2 failed .")

        my_inventory.add_inventory("Widget1", -10)
        self.assertEqual(my_inventory.items["Widget1"], 25, "Widget1 test 3 failed.")

    def test_remove_inventory_widget(self):
        my_inventory = Inventory()

        # Adding two widgets with quantities
        my_inventory.add_inventory("Widget1", 10)
        my_inventory.add_inventory("Widget2", 20)

        # Removing Widget1
        widget1_removed = my_inventory.remove_inventory_widget("Widget1", 10)
        self.assertTrue(widget1_removed, "Failed to remove Widget1.")
        self.assertEqual(len(my_inventory.items), 1, "Length of the dictionary should be 1 after removing Widget1.")
        self.assertIn("Widget2", my_inventory.items, "Widget2 should still exist in the inventory.")
