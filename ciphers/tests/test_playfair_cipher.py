import unittest

from ..alphabets import RUSSIAN_ALPHABET, ENGLISH_ALPHABET
from ..playfair_chiper import PlayfairCipher


class TestPlayfairCipher(unittest.TestCase):
    def test_encode_eng(self):
        result = PlayfairCipher.encode(
            message='ilovethisworld',
            key='superworld',
            wildcard_character='x',
            alphabet=ENGLISH_ALPHABET.replace('j', ''),
            table_size=(5, 5),
        )
        self.assertEqual('mwcusybqwbauda', result)

    def test_encode_rus(self):
        result = PlayfairCipher.encode(
            message='зашифрованноесообщение',
            key='дядина',
            wildcard_character='я',
            alphabet=RUSSIAN_ALPHABET + '-123',
            table_size=(6, 6),
        )
        self.assertEqual('жбюехсйжбаамгткапашёанги', result)

    def test_decode_eng(self):
        result = PlayfairCipher.decode(
            message='mwcusybqwbauda',
            key='superworld',
            wildcard_character='x',
            alphabet=ENGLISH_ALPHABET.replace('j', ''),
            table_size=(5, 5),
        )
        self.assertEqual('ilovethisworld', result)

    def test_decode_rus(self):
        result = PlayfairCipher.decode(
            message='жбюехсйжбаамгткапашёанги',
            key='дядина',
            wildcard_character='я',
            alphabet=RUSSIAN_ALPHABET + '-123',
            table_size=(6, 6),
        )
        self.assertEqual('зашифрованноесообщение', result)

    def test_decode_rus_2(self):
        result = PlayfairCipher.decode(
            message='звнтгщ',
            key='дедукция',
            wildcard_character='*',
            alphabet=RUSSIAN_ALPHABET.replace(
                'ё', ''
            ).replace(
                'й', ''
            ).replace(
                'ь', ''
            ),
            table_size=(6, 5),
        )
        self.assertEqual('магнит', result)
