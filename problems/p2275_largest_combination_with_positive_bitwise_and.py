class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        binary_length = max(candidates).bit_length()
        overall_max = 0
        for _ in range(binary_length):
            nb_hits = 0
            for i, candidate in enumerate(candidates):
                nb_hits += candidate % 2
                candidates[i] = candidate // 2
            overall_max = max(overall_max, nb_hits)
            if overall_max == len(candidates):
                return overall_max
        return overall_max
