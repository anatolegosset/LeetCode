class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        previous_i, previous_j = points.pop()
        result = 0
        for _ in range(len(points)):
            i, j = points.pop()
            result += max(abs(i - previous_i), abs(j - previous_j))
            previous_i, previous_j = i, j
        return result


if __name__ == '__main__':
    print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
