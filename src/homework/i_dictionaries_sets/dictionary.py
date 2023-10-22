def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The lists inputed must have the same length")
    
    number_difference = sum(1 for a, b in zip(list1, list2) if a != b)
    p_distance = number_difference / len(list1)
    return round(p_distance, 5) 

def get_p_distance_matrix(dna_sequences):
    n = len(dna_sequences)
    p_distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]

    
    for i in range(n):
        for j in range(n):
            if i == j:
                p_distance_matrix[i][j] = 0.0
            else:
                p_distance = get_p_distance(dna_sequences[i], dna_sequences[j])
                p_distance_matrix[i][j] = p_distance
        return p_distance_matrix