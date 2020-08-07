import unittest

from ..alphabets import RUSSIAN_ALPHABET, ENGLISH_ALPHABET
from ..gronsfeld_chiper import GronsfeldCipher


class TestGronsfeldCipher(unittest.TestCase):
    def test_encode(self):
        result = GronsfeldCipher.encode(
            message='GRONSFELD',
            key=2015,
            alphabet=ENGLISH_ALPHABET.upper(),
        )
        self.assertEqual('IRPSUFFQF', result)

    def test_decode(self):
        result = GronsfeldCipher.decode(
            message='дуфйупежыжфб',
            key=25357,
            alphabet=RUSSIAN_ALPHABET,
        )
        self.assertEqual('восемнадцать', result)
