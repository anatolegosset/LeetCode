class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 10
            n = n // 10
        return count
