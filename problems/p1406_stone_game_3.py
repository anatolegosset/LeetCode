class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        nb_stones = len(stoneValue)
        pouet = stoneValue
        known_values = {nb_stones: (0, 0)}

        def parcours(start):
            if start in known_values:
                return known_values[start]

            optimal_score_a = None
            overall_optimal_score_b = None
            step_score_a = 0

            for a in range(1, 4):
                if start + a > nb_stones:
                    break
                step_score_a += stoneValue[start + a - 1]
                best_b = 0
                optimal_score_b = None
                step_score_b = 0
                for b in range(1, 4):
                    if start + a + b > nb_stones:
                        break
                    step_score_b += stoneValue[start + a + b - 1]
                    _, potential_score_b = parcours(start + a + b)
                    potential_score_b += step_score_b
                    if optimal_score_b is None or potential_score_b > optimal_score_b:
                        optimal_score_b = potential_score_b
                        best_b = b
                potential_score_a, _ = parcours(start + a + best_b)
                potential_score_a += step_score_a
                if optimal_score_a is None or potential_score_a > optimal_score_a:
                    optimal_score_a = potential_score_a
                    overall_optimal_score_b = optimal_score_b
            if overall_optimal_score_b is None:
                overall_optimal_score_b = 0
            known_values[start] = (optimal_score_a, overall_optimal_score_b)
            return optimal_score_a, overall_optimal_score_b
        score_a, score_b = parcours(0)
        print(score_a, score_b)
        if score_a > score_b:
            return 'Alice'
        elif score_a < score_b:
            return 'Bob'
        else:
            return 'Tie'

