from itertools import accumulate


class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        prefix = list(accumulate(stones, initial=0))
        nb_stones = len(stones)
        dp_a = [0] * nb_stones
        dp_b = [0] * nb_stones
        for i in range(1, nb_stones):
            dp_a[i] = max(prefix[-1], max(dp_b[1:i] or [prefix[-1]]))
            dp_b[i] = min([dp_a[i-j-1] + prefix[-i-1] - prefix[j-i] for j in range(i)])

        return max(prefix[-1], max(dp_b[1:-1] or [prefix[-1]]))



