from collections import OrderedDict
from typing import Sequence


class PlayfairCipher:
    """Шифр Плейфера."""

    @classmethod
    def encode(cls,
               message: str,
               key: str,
               alphabet: str,
               table_size: Sequence,
               wildcard_character: str = '*') -> str:
        table = cls._create_table(key, alphabet, table_size)
        couples = cls._create_couples(message, wildcard_character)

        result = ''

        for couple in couples:
            p1 = cls._find_letter(couple[0], table)
            p2 = cls._find_letter(couple[1], table)

            if p1[0] == p2[0]:
                ind1 = p1[1] + 1
                ind1 = 0 if ind1 >= table_size[1] else ind1
                ind2 = p2[1] + 1
                ind2 = 0 if ind2 >= table_size[1] else ind2
                result += f'{table[p1[0]][ind1]}{table[p2[0]][ind2]}'
            elif p1[1] == p2[1]:
                ind1 = p1[0] + 1
                ind1 = 0 if ind1 >= table_size[0] else ind1
                ind2 = p2[0] + 1
                ind2 = 0 if ind2 >= table_size[0] else ind2
                result += f'{table[ind1][p1[1]]}{table[ind2][p2[1]]}'
            else:
                result += f'{table[p1[0]][p2[1]]}{table[p2[0]][p1[1]]}'

        return result

    @classmethod
    def decode(cls,
               message: str,
               key: str,
               alphabet: str,
               wildcard_character: str,
               table_size: Sequence) -> str:
        table = cls._create_table(key, alphabet, table_size)
        couples = cls._create_couples(message, wildcard_character)
        result = ''

        for couple in couples:
            p1 = cls._find_letter(couple[0], table)
            p2 = cls._find_letter(couple[1], table)

            if p1[0] == p2[0]:
                ind1 = p1[1] - 1
                ind1 = table_size[1] - 1 if ind1 < 0 else ind1
                ind2 = p2[1] - 1
                ind2 = table_size[1] - 1 if ind2 < 0 else ind2
                result += f'{table[p1[0]][ind1]}{table[p2[0]][ind2]}'
            elif p1[1] == p2[1]:
                ind1 = p1[0] - 1
                ind1 = table_size[0] - 1 if ind1 < 0 else ind1
                ind2 = p2[0] - 1
                ind2 = table_size[0] - 1 if ind2 < 0 else ind2
                result += f'{table[ind1][p1[1]]}{table[ind2][p2[1]]}'
            else:
                result += f'{table[p1[0]][p2[1]]}{table[p2[0]][p1[1]]}'

        return result.replace(wildcard_character, '')

    @staticmethod
    def _find_letter(letter: str, matrix: Sequence):
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == letter:
                    return i, j

        return None, None

    @staticmethod
    def _create_table(key: str, alphabet: str, table_size: Sequence):
        key = list(OrderedDict.fromkeys(key))
        table = [[''] * table_size[1] for _ in range(table_size[0])]
        used_letters = set(key)

        for i in range(table_size[0] * table_size[1]):
            r = i // table_size[1]
            c = i % table_size[1]

            if len(key) > i:
                table[r][c] = key[i]
                continue

            for j, letter in enumerate(alphabet):
                if letter in used_letters:
                    continue

                table[r][c] = alphabet[j]
                used_letters.add(letter)
                break

        return table

    @staticmethod
    def _create_couples(message: str, wildcard_character: str):
        couples = []
        i = 0

        while i < len(message):
            if i + 2 > len(message):
                couples.append([message[i], wildcard_character])
                break

            if message[i] == message[i + 1]:
                couples.append([message[i], wildcard_character])
                i += 1
                continue

            couples.append([
                message[i],
                message[i + 1],
            ])

            i += 2

        return couples
