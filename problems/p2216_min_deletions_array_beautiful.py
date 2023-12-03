class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = -1
        length = 0
        for num in nums:
            if num != previous or length % 2 == 0:
                previous = num
                length += 1

        length -= (length % 2 == 1)
        return len(nums) - length
