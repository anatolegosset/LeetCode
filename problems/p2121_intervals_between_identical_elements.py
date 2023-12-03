class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        partials = {}
        for i, num in enumerate(arr):
            partials.setdefault(num, [0, 0])
            partials[num].append(partials[num][-1] + i)

        for i, num in enumerate(arr):
            yield i * (2 * partials[num][0] - len(partials[num]) + 2) + partials[num][-1] - 2 * partials[num][partials[num][0] + 1]
            partials[num][0] += 1

