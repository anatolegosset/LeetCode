from collections import Counter


class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        sums.sort()
        initial = []
        current_sums = Counter(sums)
        for _ in range(n):
            keys = list(current_sums.keys())
            new = keys[1] - keys[0] if current_sums[keys[0]] == 1 else 0
            if new not in current_sums:
                new = -new
            if not new:
                for key in current_sums:
                    current_sums[key] = current_sums[key] // 2
            else:
                new_sums = Counter()
                for key in (keys if new * (keys[1] - keys[0]) < 0 else reversed(keys)):
                    new_sums[key - new] = current_sums[key] - new_sums[key]
                if new_sums[0] <= 0:
                    new = -new
                    current_sums = +(current_sums - +new_sums)
                else:
                    current_sums = +new_sums
            initial.append(new)
        return initial
