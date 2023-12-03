from math import gcd


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        d = gcd(cost1, cost2)
        cost1, cost2, total = cost1 // d, cost2 // d, total // d
        cost1, cost2 = min(cost1, cost2), max(cost1, cost2)
        if cost1 == 1:
            max_x = total // cost2
            return (max_x + 1) * (total + 1) - cost2 * (max_x * (max_x + 1)) // 2
        return sum(x // cost1 + 1 for x in range(total, -1, -cost2))
