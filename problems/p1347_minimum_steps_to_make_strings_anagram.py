from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(t) - Counter(s)).total()
