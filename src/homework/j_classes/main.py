
from class_a import Die
def main():
    die_instance = Die()

    while True:
        input("Press Enter to roll the die...")
        die_instance.roll()
        print(f"The die number rolled is: {die_instance.get_rolled_value()}")

        choice = input("Would you like to do another roll? (y/n): ").lower()
        if choice != 'y':
            print("Exiting the program.")
            break
if __name__ == "__main__":
    main()