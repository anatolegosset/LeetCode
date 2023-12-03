class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        min_sum = threshold * k
        current_sum = sum(arr[:k])
        count = int(current_sum >= min_sum)
        for i in range(len(arr) - k):
            current_sum += (arr[i + k] - arr[i])
            count += (current_sum >= min_sum)
        return count
