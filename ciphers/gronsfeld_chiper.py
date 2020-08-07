class GronsfeldCipher:
    """Шифр Гронсфельда."""

    @classmethod
    def encode(cls, message: str, key: int, alphabet: str) -> str:
        key = [int(i) for i in str(key)]
        key_size = len(key)
        alphabet_size = len(alphabet)
        result = [''] * len(message)

        for i, letter in enumerate(message):
            index = (alphabet.index(letter) + key[i % key_size]) % alphabet_size
            result[i] = alphabet[index]

        return ''.join(result)

    @classmethod
    def decode(cls, message: str, key: int, alphabet: str) -> str:
        key = [int(i) for i in str(key)]
        key_size = len(key)
        alphabet_size = len(alphabet)
        result = [''] * len(message)

        for i, letter in enumerate(message):
            index = (alphabet.index(letter) - key[i % key_size]) % alphabet_size
            result[i] = alphabet[index]

        return ''.join(result)
