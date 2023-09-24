def get_factorial(num):
    if num < 0:
        return "No negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

def sum_odd_numbers(num):
    total = 0
    current_number = 1

    while current_number <= num:
        total += current_number
        current_number += 2

    return total
