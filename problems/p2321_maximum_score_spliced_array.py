class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        current_max_1 = 0
        current_max_2 = 0

        total_diff_1 = 0
        total_diff_2 = 0
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]
            total_diff_1 += diff
            total_diff_2 -= diff
            if total_diff_1 <= 0:
                total_diff_1 = 0
            elif diff > 0:
                current_max_1 = max(current_max_1, total_diff_1)
            if total_diff_2 <= 0:
                total_diff_2 = 0
            elif diff < 0:
                current_max_2 = max(current_max_2, total_diff_2)

        return max(current_max_1 + sum(nums2), current_max_2 + sum(nums1))

