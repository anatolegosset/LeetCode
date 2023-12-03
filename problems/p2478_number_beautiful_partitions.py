from functools import cache
from itertools import accumulate


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = {'2', '3', '5', '7'}

        if s[0] not in primes or s[-1] in primes:
            return 0

        split = []
        previous = -1
        for i in range(len(s) - 1):
            if s[i] not in primes and s[i + 1] in primes:
                split.append(i - previous)
                previous = i

        split.append(len(s) - 1 - previous)
        nb_splits = len(split)
        grouped_splits = list(accumulate(split, initial=0))
        modulus = 10 ** 9 + 7

        @cache
        def parcours(start, nb_parts):
            if nb_parts == 0:
                return start == nb_splits
            current_length = 0
            total = 0
            max_previous_sum = grouped_splits[-1] - (nb_parts - 1) * minLength
            # split[start] + ... + split[j] >= min_length
            # grouped_splits[j+1] - grouped_splits[start] >= min_length
            for j in range(start, nb_splits):
                if grouped_splits[j + 1] > max_previous_sum:
                    break
                current_length += split[j]
                if current_length >= minLength:
                    total = (total + parcours(j + 1, nb_parts - 1)) % modulus
            return total
        return parcours(0, k)

