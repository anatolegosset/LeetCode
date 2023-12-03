class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        a_bitmask = 0
        b_bitmask = 0
        for a, b in zip(A, B):
            a_bitmask |= 2 ** a
            b_bitmask |= 2 ** b
            yield (a_bitmask & b_bitmask).bit_count()
