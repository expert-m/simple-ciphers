class SimpleSingleSwapPermutationCipher:
    """Шифр простой одинарной перестановки."""

    @staticmethod
    def encode(message: str, key: int) -> str:
        key = [int(item) for item in str(key)]

        assert len(message) == len(key)

        result = [''] * len(key)

        for i in range(len(key)):
            result[i] = message[key.index(i + 1)]

        return ''.join(result)

    @staticmethod
    def decode(message: str, key: int) -> str:
        key = [int(item) for item in str(key)]

        assert len(message) == len(key)

        result = [''] * len(key)

        for i in range(len(key)):
            result[key.index(i + 1)] = message[i]

        return ''.join(result)
