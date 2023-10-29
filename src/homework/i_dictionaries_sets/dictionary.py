class Inventory:
    def __init__(self):
        self.items = {}

    
    
    def test_add_inventory(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    
    
    def remove_inventory_widget(self, item, quantity_to_remove):
        if item in self.items:
            if self.items[item] >= quantity_to_remove:
                self.items[item] -= quantity_to_remove
                return True  
            else:
                return False  
        else:
            return False  