from collections import Counter


class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nb_elements = Counter()
        for num in nums:
            temp = num
            while temp > 1:
                nb_elements[temp] += 1
                temp = (temp + 2) // 3

        unique_values = sorted(nb_elements.keys(), reverse=True)
        nb_unique_values = len(unique_values)
        current_id = 0
        total = 0
        remaining_operations = k

        while remaining_operations > 0 and current_id < nb_unique_values:
            total += unique_values[current_id] * min(remaining_operations, nb_elements[unique_values[current_id]])
            remaining_operations -= min(remaining_operations, nb_elements[unique_values[current_id]])
            current_id += 1
        total += remaining_operations

        return total
