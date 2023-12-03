from itertools import accumulate


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        sums = list(accumulate(stoneValue, initial=0))
        known_values = {}

        def parcours(start, end):
            if end == start + 1:
                return 0
            if (start, end) in known_values:
                return known_values[(start, end)]

            max_score = 0
            for i in range(start + 1, end):
                right = sums[end] - sums[i]
                left = sums[i] - sums[start]
                if 2 * min(left, right) < max_score:
                    continue
                if right > left:
                    max_score = max(max_score, left + parcours(start, i))
                elif right < left:
                    max_score = max(max_score, right + parcours(i, end))
                else:
                    max_score = max(max_score, right + parcours(i, end),
                                    left + parcours(start, i))
            known_values[(start, end)] = max_score
            return max_score
        return parcours(0, len(stoneValue))
