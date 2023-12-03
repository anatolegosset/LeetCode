class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        seen = set()
        nb_nums = len(nums)
        prime = 10000001707
        total = 0
        for start in range(nb_nums):
            fake_hash = 0
            nb_divisible = 0
            for end in range(start, nb_nums):
                temp = nums[start: end]
                if nums[end] % p == 0:
                    nb_divisible += 1
                    if nb_divisible > k:
                        break
                fake_hash = (201 * fake_hash + nums[end]) % prime
                if fake_hash not in seen:
                    total += 1
                    seen.add(fake_hash)
        return total

