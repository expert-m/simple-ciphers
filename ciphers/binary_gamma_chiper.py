from typing import Sequence


class BinaryGammaCipher:
    """Двоичное гаммирование."""

    @classmethod
    def encode(cls,
               message: str,
               key: str,
               table: Sequence,
               alphabet: Sequence) -> list:
        result = []

        for i in range(len(message)):
            v1 = table[alphabet.index(message[i])]
            v2 = table[alphabet.index(key[i % len(key)])]
            result.append(v1 ^ v2)

        return result

    @classmethod
    def decode(cls,
               message: Sequence,
               key: str,
               table: Sequence,
               alphabet: Sequence) -> str:
        result = ''

        for i in range(len(message)):
            v1 = message[i]
            v2 = table[alphabet.index(key[i % len(key)])]
            result += alphabet[table.index(v1 ^ v2)]

        return result
