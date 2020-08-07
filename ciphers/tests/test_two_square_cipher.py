import unittest

from ..alphabets import ENGLISH_ALPHABET
from ..two_square_cipher import TwoSquareCipher


class TestTwoSquareCipher(unittest.TestCase):
    first_rus_table = [
        'ЖЩНЮР',
        'ИТЬЦБ',
        'ЯМЕ.С',
        'ВЫПЧ ',
        ':ДУОК',
        'ЗЭФГШ',
        'ХА,ЛЪ',
    ]

    second_rus_table = [
        'ИЧГЯТ',
        ',ЖЬМО',
        'ЗЮРВЩ',
        'Ц:ПЕЛ',
        'ЪАН.Х',
        'ЭКСШД',
        'БФУЫ ',
    ]

    first_rus_table_2 = [
        'ЫЩЭЮЬ',
        'МБГДЕ',
        'ВЖИЗК',
        'ЛСНОП',
        'АТРУФ',
        'ХЦЧШЯ',
    ]

    second_rus_table_2 = [
        'ЦЮЭЧЬ',
        'ЕМНОШ',
        'ЖЛКПЩ',
        'БВАГД',
        'РЗИФЯ',
        'СТУХЫ',
    ]

    @staticmethod
    def _create_eng_tables():
        alphabet = ENGLISH_ALPHABET.replace('q', '').upper()

        first_table = TwoSquareCipher.create_table(
            key='EXAMPLE',
            alphabet=alphabet,
            table_size=(5, 5),
        )

        second_table = TwoSquareCipher.create_table(
            key='KEYWORD',
            alphabet=alphabet,
            table_size=(5, 5),
        )

        return first_table, second_table

    def test_encode(self):
        first_table, second_table = self._create_eng_tables()

        result = TwoSquareCipher.encode(
            message='HELLOWORLD',
            first_table=first_table,
            second_table=second_table,
            is_horizontal=False,
        )

        self.assertEqual('XGNRSENDBR', result)

    def test_decode(self):
        first_table, second_table = self._create_eng_tables()

        result = TwoSquareCipher.encode(
            message='XGNRSENDBR',
            first_table=first_table,
            second_table=second_table,
            is_horizontal=False,
        )
        self.assertEqual('HELLOWORLD', result)

    def test_encode_rus(self):
        result = TwoSquareCipher.encode(
            message='ПРИЛЕТАЮ ШЕСТОГО',
            first_table=self.first_rus_table,
            second_table=self.second_rus_table,
            is_horizontal=True,
        )
        self.assertEqual('ПЕОВЩНФМЕШРФЖБДЦ', result)

    def test_decode_rus(self):
        result = TwoSquareCipher.decode(
            message='ПЕОВЩНФМЕШРФЖБДЦ',
            first_table=self.first_rus_table,
            second_table=self.second_rus_table,
            is_horizontal=True,
        )
        self.assertEqual('ПРИЛЕТАЮ ШЕСТОГО', result)

    def test_decode_rus_2(self):
        result = TwoSquareCipher.decode(
            message='ПЕФЛЗЗЫЦБУ',
            first_table=self.first_rus_table_2,
            second_table=self.second_rus_table_2,
            is_horizontal=True,
        )
        self.assertEqual('КОАГУЛЯТОР', result)
