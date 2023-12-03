class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        known_values = {}
        sums = [sum(piles)]
        for pile in piles:
            sums.append(sums[-1] - pile)
        nb_piles = len(piles)

        def parcours(start, m):
            if 2 * m >= nb_piles - start:
                return sums[start], nb_piles
            if (start, m) in known_values:
                return known_values[(start, m)]

            optimal_score = 0
            best_play = 0
            for x in range(1, 2 * m + 1):
                _, next_start = parcours(start + x, max(x, m))
                potential_score, _ = parcours(next_start, max(x, m, next_start - start - x))
                potential_score += sums[start] - sums[start + x]
                if potential_score > optimal_score:
                    optimal_score = potential_score
                    best_play = start + x
            known_values[(start, m)] = optimal_score, best_play
            return optimal_score, best_play

        return parcours(0, 1)[0]




