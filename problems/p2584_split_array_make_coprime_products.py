import math
from collections import Counter


class Solution(object):
    def findValidSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n = math.ceil(math.sqrt(max(nums)))
        root = math.ceil(math.sqrt(max_n)) + 1
        is_prime = [True] * (max_n + 1)
        primes = []
        for i in range(2, root):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False

        for j in range(root, max_n + 1):
            if is_prime[j]:
                primes.append(j)

        nb_nums = len(nums)
        starts = []
        ends = {}
        for i in range(nb_nums):
            temp = nums[i]
            for prime in primes:
                if temp % prime == 0:
                    if prime not in ends:
                        starts.append(i)
                    ends[prime] = i
                while temp % prime == 0:
                    temp = temp // prime
                if temp == 1:
                    break
            if temp > 1:
                if temp not in ends:
                    starts.append(i)
                ends[temp] = i

        counter = Counter(starts)
        counter.subtract(Counter(ends.values()))
        total = 0
        for i in range(nb_nums - 1):
            total += counter[i]
            if not total:
                return i
        return -1
