from collections import Sequence
from typing import Optional


class PortaCipher:
    """Биграммный шифр Порты."""

    @classmethod
    def encode(cls,
               message: str,
               alphabet: str,
               matrix: Optional[Sequence] = None,
               wildcard_character: str = '*') -> Sequence:
        couples = cls._create_couples(message, wildcard_character)
        result = []

        for i, couple in enumerate(couples):
            ind1 = alphabet.index(couple[0])
            ind2 = alphabet.index(couple[1])

            if matrix:
                result.append(matrix[ind1][ind2])
            else:
                result.append(len(alphabet) * ind1 + ind2 + 1)

        return result

    @classmethod
    def decode(cls,
               message: Sequence,
               alphabet: str,
               matrix: Optional[Sequence] = None) -> str:
        if isinstance(message, str):
            keys = []

            for i, letter in enumerate(message):
                if i % 3 == 0:
                    keys.append(letter)
                    continue

                keys[-1] += letter

            keys = [int(key) for key in keys]
        else:
            keys = message

        result = ''

        for i, key in enumerate(keys):
            if matrix:
                p = cls._find_item(key, matrix)
                result += alphabet[p[0]]
                result += alphabet[p[1]]
            else:
                key -= 1
                result += alphabet[key // len(alphabet)]
                result += alphabet[key % len(alphabet)]

        return result

    @staticmethod
    def _create_couples(message: str, wildcard_character: str):
        couples = []
        i = 0

        while i < len(message):
            if i + 2 > len(message):
                couples.append([message[i], wildcard_character])
                break

            couples.append([
                message[i],
                message[i + 1],
            ])

            i += 2

        return couples

    @staticmethod
    def _find_item(item: str, matrix: Sequence):
        for i, row in enumerate(matrix):
            for j, item_ in enumerate(row):
                if item_ == item:
                    return i, j

        return None, None


class PortaSecondCipher:
    """Шифр Порта. Является модификацией шифра Белазо.

    Шифрование производится с помощью секретного лозунга, который
    периодически выписывается над открытым текстом. По первой букве отыскивается
    алфавит (заглавные буквы в начале строк). В верхнем или нижнем полуалфавите
    отыскивается первая буква открытого текста и заменяется соответствующей
    ей буквой из верхней или нижней строки. Аналогично шифруются остальные
    буквы."""

    @classmethod
    def encode(cls,
               message: str,
               key: str,
               alphabet: str,
               table: Optional[Sequence] = None) -> str:
        while key and len(message) > len(key):
            key += key

        if not table:
            table = cls._create_table(alphabet)

        result = ''

        for i, letter in enumerate(message):
            index = alphabet.index(key[i])

            try:
                p = table[index].index(letter)
            except ValueError:
                index = index + 1 if index % 2 == 0 else index - 1
                p = table[index].index(letter)

            index = index + 1 if index % 2 == 0 else index - 1
            result += table[index][p]

        return result

    @classmethod
    def decode(cls,
               message: str,
               key: str,
               alphabet: str,
               table: Optional[Sequence] = None) -> str:
        return cls.encode(
            message=message,
            key=key,
            alphabet=alphabet,
            table=table,
        )

    @staticmethod
    def _create_table(alphabet: str):
        table = []
        n = len(alphabet)
        first_half = list(alphabet[:n // 2])
        second_half = list(alphabet[n // 2:])

        for i in range(n):
            if i % 2 == 0:
                table.append(first_half)
            else:
                table.append(second_half.copy())
                second_half.append(second_half.pop(0))

        return table
