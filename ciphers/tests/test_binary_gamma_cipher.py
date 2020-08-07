import unittest

from ..alphabets import RUSSIAN_ALPHABET, ENGLISH_ALPHABET
from ..binary_gamma_chiper import BinaryGammaCipher


class TestAtbashCipher(unittest.TestCase):
    def setUp(self):
        alphabet = []
        table = []

        alphabet.extend(RUSSIAN_ALPHABET.upper())
        table.extend(range(0xC0, 0xC5 + 1))
        table.append(0xA8)
        table.extend(range(0xC6, 0xDF + 1))

        alphabet.extend(RUSSIAN_ALPHABET)
        table.extend(range(0xE0, 0xE5 + 1))
        table.append(0xB8)
        table.extend(range(0xE6, 0xFF + 1))

        alphabet.extend(ENGLISH_ALPHABET.upper())
        table.extend(range(0x41, 0x5A + 1))

        alphabet.extend(ENGLISH_ALPHABET)
        table.extend(range(0x61, 0x7A + 1))

        alphabet.extend(range(0, 10))
        table.extend(range(0x30, 0x39 + 1))

        alphabet.extend(['.', ',', ':', ';', '?', '!', '…', '-', '–', '—', '_'])
        table.extend([
            0x2e, 0x2c, 0x3a, 0x3b, 0x3f,
            0x21, 0x85, 0xad, 0x96, 0x97, 0x5f,
        ])

        alphabet.extend(['«', '»', '“', '”', '‘', '’', '"', '\'', '`'])
        table.extend([0xAB, 0xBB, 0x93, 0x94, 0x91, 0x92, 0x22, 0x27, 0x60])

        alphabet.extend(['(', ')', '[', ']', '{', '}', '|'])
        table.extend([0x28, 0x29, 0x5B, 0x5D, 0x7B, 0x7D, 0x7C])

        alphabet.extend(['+', '-', '*', '/', '\\', '%', '^', '<', '>', '='])
        table.extend([
            0x2B, 0x2D, 0x2A, 0x2F, 0x5C,
            0x25, 0x5E, 0x3C, 0x3E, 0x3D,
        ])

        alphabet.extend(['~', '@', '#', '№', '&', '$'])
        table.extend([0x7E, 0x40, 0x23, 0xB9, 0x26, 0x24])

        self.alphabet = alphabet
        self.table = table

    def test_encode(self):
        result = BinaryGammaCipher.encode(
            message='Окно',
            key='Ток',
            table=self.table,
            alphabet=self.alphabet,
        )

        self.assertEqual([0x1c, 0x4, 0x7, 0x3c], result)

    def test_decode(self):
        result = BinaryGammaCipher.decode(
            message=[0x04, 0x0b, 0x02, 0x03, 0x00, 0x16],
            key='лот',
            table=self.table,
            alphabet=self.alphabet,
        )

        self.assertEqual('период', result)
