class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        previous_result = grid.pop()
        previous_min = (float('inf'), 0)
        previous_almost_min = previous_min
        for i, r in enumerate(previous_result):
            if r <= previous_min[0]:
                previous_almost_min = previous_min
                previous_min = (r, i)
            elif r <= previous_almost_min[0]:
                previous_almost_min = (r, i)
        for _ in range(n - 1):
            current_row = grid.pop()
            result = []
            new_min = (float('inf'), 0)
            new_almost_min = new_min
            for i, value in enumerate(current_row):
                if i == previous_min[1]:
                    result.append(current_row[i] + previous_almost_min[0])
                else:
                    result.append(current_row[i] + previous_min[0])
                if result[-1] <= new_min[0]:
                    new_almost_min = new_min
                    new_min = (result[-1], i)
                elif result[-1] <= new_almost_min[0]:
                    new_almost_min = (result[-1], i)
            previous_min = new_min
            previous_almost_min = new_almost_min
            previous_result = result
        return min(previous_result)
