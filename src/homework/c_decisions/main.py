import decisions 

def main():
    options = float(input("Enter the number of options: "))

    total = float(input("Enter the total number: "))

    result = decisions.get_options_ratio(options, total)

    faculty_rating = decisions.get_faculty_rating(result)

    print (f"Faculty Rating: {faculty_rating}")