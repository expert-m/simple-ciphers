class ScytaleCipher:
    """Шифр Сцитала."""

    @staticmethod
    def encode(message: str, key: int) -> str:
        k = len(message)
        n = abs((k - 1) // key) + 1
        result = [''] * k

        for i in range(len(message)):
            index = abs(key * (i % n)) + abs(i // n)

            if index < k:
                result[i] = message[index]

        return ''.join(result)

    @staticmethod
    def decode(message: str, key: int) -> str:
        k = len(message)
        n = abs((k - 1) // key) + 1
        result = [''] * k

        for i in range(len(message)):
            index = abs(key * (i % n)) + abs(i // n)

            if index < k:
                result[index] = message[i]

        return ''.join(result)
