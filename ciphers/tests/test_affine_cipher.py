import unittest

from ..affine_chiper import AffineCipher
from ..alphabets import ENGLISH_ALPHABET, RUSSIAN_ALPHABET


class TestAffineCipher(unittest.TestCase):
    def test_encode(self):
        result = AffineCipher.encode(
            message='ATTACKATDAWN',
            a=3,
            b=4,
            alphabet=ENGLISH_ALPHABET.upper()
        )
        self.assertEqual('EJJEKIEJNESR', result)

    def test_decode(self):
        result = AffineCipher.decode(
            message='нъхпз',
            a=13,
            b=4,
            alphabet=RUSSIAN_ALPHABET
        )
        self.assertEqual('приём', result)
