from math import isqrt


class BadSolution:
    def maximumSum(self, nums: list[int]):
        nb_nums = len(nums)
        max_prime = nb_nums // 4
        root = isqrt(max_prime) + 1
        is_prime = [True] * (max_prime + 1)
        primes = []
        for i in range(2, root):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, max_prime + 1, i):
                    is_prime[j] = False
        for j in range(max(2, root), max_prime + 1):
            if is_prime[j]:
                primes.append(j)
        nb_primes = len(primes)

        def parcours(previous_pid, product):
            result = 0
            for k in range(1, isqrt(nb_nums // product) + 1):
                result += nums[product * k * k - 1]
            for k in range(previous_pid + 1, nb_primes):
                new_p = product * primes[k]
                if new_p > max_prime:
                    break
                result = max(result, parcours(k, new_p))
            return result

        return max(max(nums), parcours(-1, 1))


class Solution:
    def maximumSum(self, nums: list[int]):
        nb_nums = len(nums)
        squares = [i * i for i in range(1, isqrt(nb_nums) + 1)]
        visited = [False] * nb_nums
        result = 0
        for i in range(1, nb_nums + 1):
            if not visited[i - 1]:
                temp = nums[i - 1]
                for j in range(1, isqrt(nb_nums // i)):
                    prod = i * squares[j] - 1
                    visited[prod] = True
                    temp += nums[prod]
                result = max(result, temp)
        return result

