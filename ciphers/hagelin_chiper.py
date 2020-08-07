from collections import Sequence


class HagelinCipher:
    """Шифр Бориса Хагелина"""

    @classmethod
    def encode(cls,
               message: str,
               alphabet: str,
               matrix: Sequence,
               stepic_matrix: Sequence) -> str:
        h_arr = cls.multiply_matrix(matrix, stepic_matrix)

        result = ''

        for i, letter in enumerate(message):
            m = (h_arr[i] - alphabet.index(letter) - 1) % len(alphabet)
            result += alphabet[m]

        return result

    @classmethod
    def decode(cls,
               message: str,
               alphabet: str,
               matrix: Sequence,
               stepic_matrix: Sequence) -> str:
        return cls.encode(
            message=message,
            alphabet=alphabet,
            matrix=matrix,
            stepic_matrix=stepic_matrix,
        )

    @staticmethod
    def multiply_matrix(matrix: Sequence, stepic_matrix: Sequence):
        n = len(matrix[0])
        m = len(stepic_matrix[-1]) + 1
        result = []

        for i in range(m):
            r = 0

            for j in range(n):
                for k in range(6):
                    v1 = matrix[k][j]
                    v2 = stepic_matrix[k][i] if len(stepic_matrix[k]) > i else 0

                    if v1 and v2:
                        r += 1
                        break

            result.append(r)

        return result
