import random
from typing import Sequence


class HomophonicSubstitutionCipher:
    """Шифр многозначной замены."""

    @classmethod
    def encode(cls, message: Sequence, alphabet: str, table: Sequence) -> list:
        result = []

        for letter in message:
            index = alphabet.index(letter)
            result.append(random.choice(table[index]))

        return result

    @classmethod
    def decode(cls, message: Sequence, alphabet: str, table: Sequence) -> str:
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

        table = [set(row) for row in table]
        result = ''

        for key in keys:
            for i, row in enumerate(table):
                if key in row:
                    result += alphabet[i]
                    break

        return result
