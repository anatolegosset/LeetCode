from collections import Counter
from functools import reduce


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        return reduce(lambda x, y: ((x + y) % (10 ** 9 + 7)), (((v * (v - 1)) // 2) for v in Counter((num - int(str(num)[::-1]) for num in nums)).values()))
