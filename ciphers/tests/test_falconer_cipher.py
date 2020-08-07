import unittest

from ..alphabets import RUSSIAN_ALPHABET
from ..falconer_chiper import FalconerCipher


class TestFalconerCipher(unittest.TestCase):
    def test_encode_1(self):
        result = FalconerCipher.encode(
            'ШИФРВЕРТИКАЛЬНОЙПЕРЕСТАНОВКИ',
            'ЛИЛИПУТ',
            RUSSIAN_ALPHABET.upper(),
        )
        self.assertEqual('ИИЙАРАЕОШТОТФКПНВЛРВРНСИЕЬЕК', result)

    def test_decode(self):
        result = FalconerCipher.decode(
            'йукабениимщдзисдунливймчаираровглсоусеммоиюсё',
            'лейтенант',
            RUSSIAN_ALPHABET,
        )
        self.assertEqual('ведущийвойнусдругиминезаключилмирассамимсобоё', result)
