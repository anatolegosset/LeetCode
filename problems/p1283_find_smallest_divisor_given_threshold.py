import math


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        if threshold == len(nums):
            return max(nums)
        s = sum(nums)
        start = math.ceil(s / threshold)
        end = math.ceil(s / (threshold - len(nums)) + 1)

        while True:
            if start + 1 == end:
                return start
            mid = (start + (end - start - 1) // 2)
            if sum(((num + mid - 1) // mid for num in nums)) > threshold:
                start = mid + 1
            else:
                end = mid + 1


