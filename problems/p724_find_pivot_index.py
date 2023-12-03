class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_right = sum(nums[1:])
        if sum_right == 0:
            return 0
        sum_left = 0
        for i in range(len(nums) - 1):
            sum_left += nums[i]
            sum_right -= nums[i + 1]
            if sum_left == sum_right:
                return i + 1
        return -1
