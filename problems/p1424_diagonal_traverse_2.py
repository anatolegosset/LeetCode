class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        full_list = []
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                full_list.append((i + j, j))
        full_list.sort()
        return (nums[a - b][b] for a, b in full_list)