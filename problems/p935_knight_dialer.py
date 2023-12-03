class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        can_reach = [[4, 5], [5, 7], [6, 8], [4, 7], [0, 3, 8], [0, 1, 6], [2, 5], [1, 3], [2, 4]]
        previous = [1] * 10
        prime = 10 ** 9 + 7
        for _ in range(n - 1):
            current = []
            for i in range(9):
                current.append(sum(previous[j] for j in can_reach[i]) % prime)
            previous = current
        return sum(previous) % prime
