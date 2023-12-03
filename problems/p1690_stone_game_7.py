class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        nb_stones = len(stones)
        if nb_stones % 2 == 0:
            dp = list(stones)
            for interval_length in range(1, nb_stones, 2):
                for i in range(nb_stones - interval_length):
                    dp[i] = max(dp[i], dp[i + 1])
                for i in range(nb_stones - interval_length - 1):
                    dp[i] = min(stones[i] + dp[i + 1], stones[i + interval_length + 1] + dp[i])
                dp[0] = max(dp[0], dp[1])
        else:
            dp = [0] * nb_stones
            for interval_length in range(1, nb_stones, 2):
                for i in range(nb_stones - interval_length):
                    dp[i] = min(stones[i] + dp[i + 1], stones[i + interval_length] + dp[i])
                for i in range(nb_stones - interval_length - 1):
                    dp[i] = max(dp[i], dp[i + 1])

        return dp[0]
