import math


class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2

        divisors = []
        for i in range(2 * n):
            divisors.append([])
            for j in range(i + 1, 2 * n):
                divisors[i].append(math.gcd(nums[i], nums[j]))
        # pgcd(nums[i], nums[j]) = divisors[i][j - i - 1]

        known_values = {4 ** n - 1: 0}

        def parcours(previous_gcd, depth, previous_bitmask, previous_a):
            if previous_bitmask in known_values:
                return known_values[previous_bitmask]

            max_score = 0
            for a in range(2 * n):
                new_bitmask = previous_bitmask | (1 << a)
                if previous_bitmask & (1 << a):
                    continue
                for b in range(a + 1, 2 * n):
                    if previous_bitmask & (1 << b):
                        continue
                    potential_gcd = divisors[a][b - a - 1]
                    new_bitmask = new_bitmask | (1 << b)
                    max_score = max(max_score, depth * potential_gcd + parcours(potential_gcd, depth - 1, new_bitmask, a))
                    new_bitmask = new_bitmask ^ (1 << b)
            known_values[previous_bitmask] = max_score
            return max_score
        return parcours(-1, n, 0, -1)
