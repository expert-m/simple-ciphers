import unittest

from ..alphabets import RUSSIAN_ALPHABET
from ..atbash_chiper import AtbashCipher


class TestAtbashCipher(unittest.TestCase):
    def test_encode(self):
        result = AtbashCipher.encode('привет', RUSSIAN_ALPHABET)
        self.assertEqual('поцэъм', result)

    def test_decode(self):
        result = AtbashCipher.decode('юцриъсрч', RUSSIAN_ALPHABET)
        self.assertEqual('биоценоз', result)
