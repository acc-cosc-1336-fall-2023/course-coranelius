from dictionary import get_p_distance_matrix

def get_user_input():
    try:
        option = int(input("Menu:\n1- Get p distance matrix\n2- Exit\nChoose an option: "))
        return option
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return -1

def main():
    while True:
        option = get_user_input()

        if option == 1:       
            dna_sequences = input("Enter the DNA sequences separated by spaces: ").split()
            dna_sequences = [list(sequence) for sequence in dna_sequences]

            p_distance_matrix = get_p_distance_matrix(dna_sequences)

            for row in p_distance_matrix:
                print(" ".join(map(str, row)))
        elif option == 2:
            print("Leaving program.")
            break
        else:
            print("Invalid option. Enter 1 or 2: ")

if __name__ == "__main__":
    main()