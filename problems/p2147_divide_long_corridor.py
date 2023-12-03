from functools import reduce


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        return reduce(lambda x, y: x * (len(y) + 1), (a := corridor.strip('P').split('S'))[2:-1:2], (len(a) % 2) * (len(a) > 1))