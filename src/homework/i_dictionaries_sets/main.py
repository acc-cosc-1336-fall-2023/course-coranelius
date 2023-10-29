
from dictionary import Inventory
inventory = Inventory()
while True:
        print("Inventory Menu")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        
        choice = input("Enter your choice here: ")
        
        if choice == "1":
            item = input("Enter item name here: ")
            quantity = int(input("Enter quantity in order too add/update: "))
            inventory.test_add_inventory(item, quantity)
            print(f"{item} with quantity {quantity} added/updated in the inventory.")
        elif choice == "2":
            item = input("Enter item to delete: ")
            if item in inventory.items:
                del inventory.items[item]
                print(f"{item} has been removed from the inventory.")
            else:
                print(f"{item} has not been found in the inventory.")
        elif choice == "3":
            print("Leaving the program")
            break
        else:
            print("Invalid choice. Please enter either 1, 2, or 3.")