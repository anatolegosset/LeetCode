class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        result = sum((len(g) for g in garbage)) + 3 * sum(travel)
        remaining = {'P', 'G', 'M'}.difference(set(garbage[-1]))
        i = -1
        while remaining:
            remaining = remaining.difference(set(garbage[i]))
            result -= travel[i] * len(remaining)
            i -= 1
        return result



