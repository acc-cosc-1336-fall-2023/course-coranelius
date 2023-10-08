from strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("Menu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            distance = get_hamming_distance(dna1, dna2)
            print(f"Hamming Distance: {distance}")
        
        elif choice == '2':
            dna = input("Enter the DNA string: ")
            complement = get_dna_complement(dna)
            print(f"DNA Complement: {complement}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")
if __name__ == "__main__":
    main()