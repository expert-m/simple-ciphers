import unittest

import numpy as np

from ..alphabets import RUSSIAN_ALPHABET
from ..porta_chiper import PortaCipher, PortaSecondCipher


class TestPortaCipherCipher(unittest.TestCase):
    alphabet = RUSSIAN_ALPHABET.replace('ё', '').replace('й', '')

    def test_encode(self):
        result = PortaCipher.encode(
            message='супер'.lower(),
            alphabet=self.alphabet,
            wildcard_character='я',
        )

        self.assertEqual([515, 440, 496], result)

    def test_decode(self):
        result = PortaCipher.decode(
            message='515440496',
            alphabet=self.alphabet,
        )

        self.assertEqual('суперя', result)

    def test_decode_2(self):
        alphabet = RUSSIAN_ALPHABET.replace(
            'ё', ''
        ).replace(
            'й', ''
        ).replace(
            'ъ', ''
        )
        n = len(alphabet)
        matrix = list(np.arange(n ** 2).reshape((n, n)) + 100)

        result = PortaCipher.decode(
            message=[610, 464, 261],
            alphabet=self.alphabet,
            matrix=matrix,
        )

        self.assertEqual('тандем', result)


class TestPortaSecondCipherCipher(unittest.TestCase):
    alphabet = RUSSIAN_ALPHABET.replace('ё', '')

    def test_encode(self):
        result = PortaSecondCipher.encode(
            message='периодическийшифр',
            key='философияфилософи',
            alphabet=self.alphabet,
        )

        self.assertEqual('щщляцытгфзюэраякм', result)

    def test_decode(self):
        result = PortaSecondCipher.decode(
            message='щщляцытгфзюэраякм',
            key='философияфилософи',
            alphabet=self.alphabet,
        )

        self.assertEqual('периодическийшифр', result)

    def test_decode_2(self):
        result = PortaSecondCipher.decode(
            message='фххфнръьюхяхчтоыуэьэяш',
            key='обозрение',
            alphabet=self.alphabet,
        )

        self.assertEqual('необходимоподкрепление', result)

