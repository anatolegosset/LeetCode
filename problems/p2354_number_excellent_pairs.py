import operator
from bisect import bisect_left
from collections import Counter
from itertools import accumulate


class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        nums = Counter((num.bit_count() for num in set(nums)))
        total_distinct_numbers = sum(nums.values())
        nums = list(nums.items())
        nums.sort()
        suffixes = list(accumulate([j for _, j in nums], func=operator.sub, initial=total_distinct_numbers))

        total = 0
        for i, (nb_bits, nb_with_nb_bits) in enumerate(nums):
            j = bisect_left(nums, k - nb_bits, key=lambda x: x[0])
            if i < j:
                total += nb_with_nb_bits * suffixes[j] * 2
            else:
                total += suffixes[i] * suffixes[i]
                break
        return total
