from collections import Counter


class Solution:
    def minOperations(self, nums: list[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        nums = Counter(nums)
        current_digit = 1
        nb_ops = 0
        from_previous_digits = 0
        while current_digit <= target:
            from_previous_digits += current_digit * nums[current_digit]
            if target & current_digit:
                if from_previous_digits >= current_digit:
                    from_previous_digits -= current_digit
                    current_digit *= 2
                else:
                    from_previous_digits += current_digit
                    while nums[current_digit] == 0:
                        nb_ops += 1
                        nums[current_digit] += 1
                        current_digit *= 2
                    nums[current_digit] -= 1
            else:
                current_digit *= 2
        return nb_ops




