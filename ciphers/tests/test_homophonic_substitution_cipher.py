import unittest

from ..alphabets import RUSSIAN_ALPHABET
from ..homophonic_substitution_cipher import HomophonicSubstitutionCipher


class TestHomophonicSubstitutionCipher(unittest.TestCase):
    table = [
        [
            315, 432, 558, 704, 801, 575, 838, 707,
            638, 731, 639, 884, 598, 824, 841, 620,
        ],  # а
        [105, 373, 854, 889],  # б
        [438, 500, 567, 757, 891, 644, 849, 892, 783],  # в
        [341, 512, 894, 797],  # г
        [101, 515, 853, 893, 856, 637],  # д,
        [
            145, 517, 411, 525, 794, 882, 728, 850,
            618, 812, 610, 724, 792, 595, 615, 897, 741,
        ],  # е
        [417],  # ё
        [425, 873],  # ж
        [248, 530, 754, 883],  # з
        [
            337, 386, 531, 587, 782, 852, 629,
            809, 753, 652, 903, 585, 723, 826, 879,
        ],  # и
        [390, 904, 823],  # й
        [155, 533, 752, 907, 667, 778, 908],  # к
        [485, 536, 909, 808, 914, 864, 668, 878, 788],  # л
        [293, 552, 867, 616, 736, 916, 923],  # м
        [
            483, 924, 737, 822, 926, 821, 917,
            819, 927, 605, 717, 863, 627, 928,
        ],  # н
        [
            100, 505, 314, 234, 415, 104, 355, 522, 580,
            929, 777, 931, 829, 719, 671, 932, 625, 837,
            725, 995,
        ],  # o
        [348, 672, 933, 807, 934, 872],  # п
        [405, 936, 784, 937, 686, 938, 708, 688, 876, 713],  # р
        [255, 702, 939, 617, 942, 857, 646, 818, 943, 859, 944],  # с
        [481, 816, 871, 868, 679, 803, 946, 947, 647, 948, 732, 742, 635],  # т
        [275, 874, 621, 798, 949, 831],  # у
        [447],  # ф
        [102, 744],  # х
        [467],  # ц,
        [320, 814, 953],  # ч
        [177, 651],  # ш
        [465],  # щ
        [282],  # ъ
        [450, 954, 711, 836],  # ы
        [103, 834, 957, 628],  # ь
        [499],  # э
        [325, 743],  # ю
        [391, 858, 709, 969],  # я
    ]

    def test_encode(self):
        result = HomophonicSubstitutionCipher.encode(
            message='сегмент',
            alphabet=RUSSIAN_ALPHABET,
            table=self.table,
        )

        result = HomophonicSubstitutionCipher.decode(
            message=result,
            alphabet=RUSSIAN_ALPHABET,
            table=self.table,
        )

        self.assertEqual('сегмент', result)

    def test_decode(self):
        result = HomophonicSubstitutionCipher.decode(
            message='939145512552741822868',
            alphabet=RUSSIAN_ALPHABET,
            table=self.table,
        )
        self.assertEqual('сегмент', result)
