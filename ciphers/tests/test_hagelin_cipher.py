import unittest

from ..alphabets import ENGLISH_ALPHABET
from ..hagelin_chiper import HagelinCipher


class TestHagelinCipher(unittest.TestCase):
    matrix = [
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
            1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1,
            1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 1, 0, 0, 0],
    ]

    matrix_2 = [
        '000100001010001110000000001',
        '100010001001100010010010100',
        '000000000000000000000000000',
        '001100010100001001000111111',
        '001010000001000100100000000',
        '000000010010010000010001000',
    ]

    stepic_matrix = [
        '01100010000000110',
        '0111110000000000000',
        '001000001000000000000',
        '00000000000100100010001',
        '1010000000000000000000000',
        '11000000000000100010000001',
    ]

    stepic_matrix_2 = [
        '01100010000000110011000100000001100110001000000',
        '01111100000000000000111110000000000000011111000',
        '00100000100000000000000100000100000000000000100',
        '00000000000100100010001000000000001001000100010',
        '10100000000000000000000001010000000000000000000',
        '11000000000000100010000001110000000000001000100',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, row in enumerate(self.stepic_matrix):
            self.stepic_matrix[i] = [
                int(i) for i in row
            ]

        for i, row in enumerate(self.stepic_matrix_2):
            self.stepic_matrix_2[i] = [
                int(i) for i in row
            ]

        for i, row in enumerate(self.matrix_2):
            self.matrix_2[i] = [
                int(i) for i in row
            ]

    def test_encode(self):
        result = HagelinCipher.encode(
            message='themobilephoneisswitchedoff',
            alphabet=ENGLISH_ALPHABET,
            matrix=self.matrix,
            stepic_matrix=self.stepic_matrix,
        )

        self.assertEqual('rjnvtgyowksxmvkohdggxshwlzu', result)

    def test_decode(self):
        result = HagelinCipher.decode(
            message='rjnvtgyowksxmvkohdggxshwlzu',
            alphabet=ENGLISH_ALPHABET,
            matrix=self.matrix,
            stepic_matrix=self.stepic_matrix,
        )

        self.assertEqual('themobilephoneisswitchedoff', result)

    def test_decode_2(self):
        result = HagelinCipher.decode(
            message='dcuervuvmglggsnrvlcvehuubfpflkocgmibsugbmdeupav',
            alphabet=ENGLISH_ALPHABET,
            matrix=self.matrix_2,
            stepic_matrix=self.stepic_matrix_2,
        )

        self.assertEqual(
            'governmentofthepeoplebythepeopleandforthepeople',
            result,
        )
