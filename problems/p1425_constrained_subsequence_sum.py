from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        dp = deque()
        dp.append((0, nums[0]))
        result = nums[0]
        for i, num in enumerate(nums[1:]):
            while dp and dp[0][0] < i + 1 - k:
                dp.popleft()
            new_value = nums[i + 1] + max(0, dp[0][1])
            result = max(result, new_value)
            while dp and dp[-1][1] <= new_value:
                dp.pop()
            dp.append((i + 1, new_value))
        return result
