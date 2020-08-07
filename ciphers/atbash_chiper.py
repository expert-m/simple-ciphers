class AtbashCipher:
    """Шифр Атбаш."""

    @classmethod
    def encode(cls, message: str, alphabet: str) -> str:
        result = ''

        for letter in message:
            index = len(alphabet) - alphabet.index(letter) - 1
            result += alphabet[index]

        return result

    @classmethod
    def decode(cls, message: str, alphabet: str) -> str:
        return cls.encode(message=message, alphabet=alphabet)
