import unittest

from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement


class Test_Config(unittest.TestCase):
    def test_get_hamming_distance(self):
        dna1 = "GAGCCTACTAACGGGAT"
        dna2 = "CATCGTAATGACGGCCT"
        
        expected_distance = 7

        real_distance = get_hamming_distance(dna1, dna2)

       
        self.assertEqual(real_distance, expected_distance)

    def test_get_dna_complement(self):
        dna = "AAAACCCGGT"
        expected_complement = "ACCGGGTTTT"
        
        complement = get_dna_complement(dna)
        
        self.assertEqual(complement, expected_complement)
    