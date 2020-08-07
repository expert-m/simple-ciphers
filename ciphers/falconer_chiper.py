import numpy as np


class FalconerCipher:
    """Шифр Фальконера."""

    @classmethod
    def encode(cls, message: str, key: str, alphabet: str) -> str:
        key = cls._get_key(key, alphabet)
        table = cls._get_table(message, key)
        shape = table.shape

        result = ''

        for i in range(shape[1]):
            for j in range(shape[0]):
                index = key.index(i)
                result += table[j][index]

        return result

    @classmethod
    def decode(cls, message: str, key: str, alphabet: str) -> str:
        key = cls._get_key(key, alphabet)
        table = cls._get_table(message, key)
        table = table.reshape(table.shape[::-1]).transpose()
        shape = table.shape

        result = ''

        for j in range(shape[0]):
            for i in key:
                result += table[j][i]

        return result

    @staticmethod
    def _get_key(key: str, alphabet: str) -> list:
        key = list(key)
        sorted_key = sorted(key, key=lambda l: alphabet.index(l))
        processed_ids = set()

        for i, new_letter in enumerate(sorted_key):
            for j, old_letter in enumerate(key):
                if j in processed_ids:
                    continue

                if old_letter == new_letter:
                    key[j] = i
                    processed_ids.add(j)
                    break

        return key

    @staticmethod
    def _get_table(message: str, key: list) -> np.array:
        m = len(key)
        n = len(message) // m

        if n * m < len(message):
            m += 1

        arr = list(message) + [''] * (n * m - len(message))
        return np.array(arr).reshape((n, m))
