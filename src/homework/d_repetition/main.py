import unittest
from repetition import sum_odd_numbers, get_factorial

def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        if 0 <= num <= 10:
            result = get_factorial(num)
            print(f"The factorial of {num} is {result}")
        else:
            print("Please enter a number between 0 and 10.")

    elif choice == "2":
        num = int(input("Enter a number: "))
        if 0 <= num <= 100:
            result = sum_odd_numbers(num)
            print(f"The sum of odd numbers up to {num} is {result}")
        else:
            print("Please enter a number between 0 and 100.")

    elif choice == "3":
        while True:
            continue_option = input("Would you like to continue (yes/no)?: ")
            if continue_option == "no":
                print("Exiting")
                

            elif continue_option == "yes":
                break  

            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
