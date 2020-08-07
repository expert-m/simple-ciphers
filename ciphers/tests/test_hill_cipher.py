import unittest

from ..alphabets import ENGLISH_ALPHABET
from ..hill_chiper import HillCipher


class TestHillCipher(unittest.TestCase):
    key = [
        [4, 5, 6],
        [8, 2, 3],
        [7, 1, 9],
    ]

    def test_encode(self):
        result = HillCipher.encode(
            message='act',
            key='gybnqkurp',
            alphabet=ENGLISH_ALPHABET,
        )

        self.assertEqual('poh', result)

    def test_decode(self):
        result = HillCipher.decode(
            message='poh',
            key='gybnqkurp',
            alphabet=ENGLISH_ALPHABET,
        )

        self.assertEqual('act', result)

    # def test_simple_decode(self):
    #     result = HillCipher.simple_decode(
    #         message=[28, 40, 44, 48, 168, 120],
    #         key=[[2, 2, 3], [3, 7, 4], [2, 5, 7]],
    #         alphabet=ENGLISH_ALPHABET,
    #     )
    #
    #     self.assertEqual('act', result)
