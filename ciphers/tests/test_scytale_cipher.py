import unittest

from ..scytale_cipher import ScytaleCipher


class TestScytaleCipher(unittest.TestCase):
    def test_encode_1(self):
        result = ScytaleCipher.encode('НАС АТАКУЮТ', 4)
        self.assertEqual('НАУАТЮСАТ К', result)

    def test_encode_2(self):
        result = ScytaleCipher.encode('РАКЕТНЫЕ_ВОЙСКА', 5)
        self.assertEqual('РНОАЫЙКЕСЕ_КТВА', result)

    def test_decode(self):
        result = ScytaleCipher.decode('РНОАЫЙКЕСЕ КТВА', 5)
        self.assertEqual('РАКЕТНЫЕ ВОЙСКА', result)
