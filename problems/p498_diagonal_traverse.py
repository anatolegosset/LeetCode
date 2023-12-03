class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        up = True
        for k in range(m + n):
            if up:
                for i in range(min(m, k + 1) - 1, max(0, k - n + 1) - 1, -1):
                    yield mat[i][k - i]
            else:
                for i in range(max(0, k - n + 1), min(m, k + 1)):
                    yield mat[i][k - i]
            up = not up
