from math import gcd
from collections import Counter


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        nb_points = len(points)
        max_colinear = 1

        def std_rep(a, b):
            new_a, new_b = a // gcd(a, b), b // gcd(a, b)
            if new_b < 0 or new_b == 0 and new_a < 0:
                new_a, new_b = -new_a, -new_b
            return new_a, new_b

        for i in range(nb_points):
            count_hits = Counter()
            for j in range(i + 1, nb_points):
                x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
                count_hits[std_rep(x, y)] += 1
            max_colinear = max(max_colinear, 1 + max(count_hits.values() or [0]))

        return max_colinear
