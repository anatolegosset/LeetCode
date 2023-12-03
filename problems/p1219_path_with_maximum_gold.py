from itertools import chain


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])

        def backtrack(i, j):
            result = 0
            temp = grid[i][j]
            grid[i][j] = 0
            for step in steps:
                next_i, next_j = i + step[0], j + step[1]
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j]:
                    result = max(result, backtrack(next_i, next_j))
            grid[i][j] = temp
            return result + temp

        return max(chain((backtrack(i // n, i % n) for i in range(n*m) if grid[i // n][i % n]), [0]))

