from math import isqrt
from bisect import bisect_right


class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        if any(num <= i for i, num in enumerate(nums)):
            return False
        for _ in range(len(nums) - 1):
            a = nums.pop()
            if a <= nums[-1]:
                nums.append(a)
                break
        if len(nums) == 1:
            return True
        max_prime = max(nums)
        root = isqrt(max_prime) + 1
        is_prime = [True] * (max_prime + 1)
        primes = [0]
        for i in range(2, root):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, max_prime + 1, i):
                    is_prime[j] = False
        for j in range(max(2, root), max_prime + 1):
            if is_prime[j]:
                primes.append(j)

        previous = 1
        for num in nums:
            if previous > num:
                return False
            prime = primes[bisect_right(primes, num - previous) - 1]
            previous = num - prime + 1
        return True

