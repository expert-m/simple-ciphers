import unittest

from ..simple_single_swap_permutation_cipher import (
    SimpleSingleSwapPermutationCipher,
)


class TestSimpleSingleSwapPermutationCipher(unittest.TestCase):
    def test_encode(self):
        result = SimpleSingleSwapPermutationCipher.encode('АБРАМОВ', 2417653)
        self.assertEqual('РАВБОМА', result)

    def test_decode(self):
        result = SimpleSingleSwapPermutationCipher.decode('РАВБОМА', 2417653)
        self.assertEqual('АБРАМОВ', result)
