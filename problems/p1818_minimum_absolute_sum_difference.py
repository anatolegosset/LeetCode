from bisect import bisect_left


class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nb_nums = len(nums1)
        nums1, nums2 = zip(*sorted(zip(nums1, nums2)))
        abs_diff = 0
        best_diff = 0
        for i in range(nb_nums):
            abs_diff += abs(nums1[i] - nums2[i])
            new_id = bisect_left(nums1, nums2[i])
            if new_id > 0:
                best_diff = max(best_diff, abs(nums1[i] - nums2[i]) - abs(nums1[new_id - 1] - nums2[i]))
            if new_id < nb_nums:
                best_diff = max(best_diff, abs(nums1[i] - nums2[i]) - abs(nums1[new_id] - nums2[i]))
        return (abs_diff - best_diff) % (10 ** 9 + 7)
