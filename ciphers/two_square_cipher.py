from collections import Sequence

from .playfair_chiper import PlayfairCipher


class TwoSquareCipher(PlayfairCipher):
    """Шифр Уитстона."""

    @classmethod
    def encode(cls,
               message: str,
               first_table: Sequence,
               second_table: Sequence,
               is_horizontal: bool = True,
               wildcard_character: str = '*') -> str:
        couples = cls._create_couples(message, wildcard_character)

        result = ''

        for couple in couples:
            p1 = cls._find_letter(couple[0], first_table)
            p2 = cls._find_letter(couple[1], second_table)

            if is_horizontal:
                if p1[0] == p2[0]:
                    result += second_table[p1[0]][p1[1]]
                    result += first_table[p2[0]][p2[1]]
                elif p1[1] == p2[1]:
                    result += second_table[p1[0]][p1[1]]
                    result += first_table[p2[0]][p2[1]]
                else:
                    result += second_table[p1[0]][p2[1]]
                    result += first_table[p2[0]][p1[1]]
            else:
                if p1[0] == p2[0]:
                    result += first_table[p2[0]][p2[1]]
                    result += second_table[p1[0]][p1[1]]
                elif p1[1] == p2[1]:
                    result += first_table[p2[0]][p2[1]]
                    result += second_table[p1[0]][p1[1]]
                else:
                    result += first_table[p1[0]][p2[1]]
                    result += second_table[p2[0]][p1[1]]

        return result

    @classmethod
    def decode(cls,
               message: str,
               first_table: Sequence,
               second_table: Sequence,
               is_horizontal: bool,
               wildcard_character: str = '*') -> str:
        return cls.encode(
            message=message,
            first_table=second_table,
            second_table=first_table,
            is_horizontal=is_horizontal,
            wildcard_character=wildcard_character,
        )

    @classmethod
    def create_table(cls,
                     key: str,
                     alphabet: str,
                     table_size: Sequence):
        return cls._create_table(
            key=key,
            alphabet=alphabet,
            table_size=table_size,
        )

    @staticmethod
    def _create_couples(message: str, wildcard_character: str):
        couples = []
        i = 0

        while i < len(message):
            if i + 2 > len(message):
                couples.append([message[i], wildcard_character])
                break

            couples.append([
                message[i],
                message[i + 1],
            ])

            i += 2

        return couples
