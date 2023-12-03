class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        dict_mapping = {str(i): str(digit) for i, digit in enumerate(mapping)}

        def shuffle(num):
            return int("".join([dict_mapping[char] for char in str(num)]))

        nums.sort(key=shuffle)
        return nums
