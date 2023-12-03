class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start = 0
        end = len(arr)
        while True:
            if end == start:
                return start
            third_1 = (2 * start + end) // 3
            third_2 = max((start + 2 * end) // 3, third_1 + 1)
            if arr[third_2] > arr[third_1]:
                start = third_1 + 1
            else:
                end = third_2 - 1

