class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        result = []
        agg = 0
        for num in word:
            agg = (agg * 10 + int(num)) % m
            result.append(int(not agg))
        return result
