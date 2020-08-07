class AffineCipher:
    """Аффинный шифр."""

    @classmethod
    def encode(cls, message: str, a: int, b: int, alphabet: str) -> str:
        n = len(alphabet)
        result = ''

        for i, letter in enumerate(message):
            index = (a * alphabet.index(letter) + b) % n
            result += alphabet[index]

        return result

    @classmethod
    def decode(cls, message: str, a: int, b: int, alphabet: str) -> str:
        n = len(alphabet)
        new_a = cls._bezout(a, n)[0]
        result = ''

        for i, letter in enumerate(message):
            index = new_a * (alphabet.index(letter) - b) % n
            result += alphabet[int(index)]

        return result

    @staticmethod
    def _bezout(a: int, b: int) -> tuple:
        """An implementation of extended Euclidean algorithm.

        Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b)."""
        x, xx, y, yy = 1, 0, 0, 1

        while b:
            q = a // b
            a, b = b, a % b
            x, xx = xx, x - xx * q
            y, yy = yy, y - yy * q

        return x, y, a
