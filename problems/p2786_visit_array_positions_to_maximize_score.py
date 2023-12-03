class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        max_even = 0
        max_odd = 0
        for _ in range(len(nums)):
            num = nums.pop()
            if num % 2 == 0:
                max_even = num + max(max_even, max_odd - x)
            else:
                max_odd = num + max(max_odd, max_even - x)
        if num % 2 == 0:
            return max_even
        else:
            return max_odd

