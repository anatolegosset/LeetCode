class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        result = 1
        nums.sort()
        current_max = nums[0] + k
        for num in nums:
            if num > current_max:
                current_max = num + k
                result += 1
        return result

