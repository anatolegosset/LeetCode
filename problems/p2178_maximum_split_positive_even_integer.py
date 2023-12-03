from math import isqrt
from itertools import chain


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if finalSum % 2 == 1:
            return []

        n = (isqrt(1 + 4 * finalSum) - 1) // 2 - 1

        result = range(2, 2 * n + 2, 2)

        return chain(result, [finalSum - n * (n+1)])

