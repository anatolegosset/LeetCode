class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        dp = [(0, 0)] * length
        for i in range(1, length):
            for j in range(length - i):
                if s[j] == s[j + i]:
                    dp[j] = (dp[j + 1][1], dp[j][0])
                else:
                    dp[j] = (min(dp[j][0], dp[j + 1][0]) + 1, dp[j][0])
        return dp[0][0]
