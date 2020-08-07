import numpy as np
from sympy import Matrix


class HillCipher:
    """Шифр Хилла."""

    @classmethod
    def encode(cls, message: str, key: str, alphabet: str) -> str:
        key = np.array([alphabet.index(i) for i in key]).reshape((3, 3))
        message = [alphabet.index(i) for i in message]
        message = np.array(message).reshape((len(message) // 3, 3))
        result = []

        for row in message:
            result.extend(np.matmul(key, row.transpose()))

        return ''.join([alphabet[i % len(alphabet)] for i in result])

    @classmethod
    def decode(cls, message: str, key: str, alphabet: str) -> str:
        key = np.array([alphabet.index(i) for i in key]).reshape((3, 3))

        key = Matrix(key).inv_mod(len(alphabet))

        message = [alphabet.index(i) for i in message]
        message = np.array(message).reshape((len(message) // 3, 3))
        message = [Matrix(row) for row in message]
        result = []

        for row in message:
            result.extend(key * row)

        return ''.join([alphabet[i % len(alphabet)] for i in result])

    @classmethod
    def simple_decode(cls, message: list, key: list, alphabet: str) -> str:
        key = Matrix(key).inv_mod(len(alphabet))
        message = np.array(message).reshape((len(message) // 3, 3))
        message = [Matrix(row) for row in message]

        result = []

        for row in message:
            result.extend(key * row)

        return ''.join([alphabet[i % len(alphabet)] for i in result])
