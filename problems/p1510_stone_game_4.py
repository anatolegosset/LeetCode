from math import isqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        is_winning = [0] * (n + 1)

        for i in range(1, n + 1):
            for nb_removed in range(1, isqrt(i) + 1):
                if is_winning[i - nb_removed * nb_removed] == 0:
                    is_winning[i] = 1
                    break
        return is_winning[n] == 1
