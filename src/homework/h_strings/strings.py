
def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance

def get_dna_complement(dna):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_dna = ''.join(complement_dict[base] for base in reversed(dna))
    return complemented_dna
