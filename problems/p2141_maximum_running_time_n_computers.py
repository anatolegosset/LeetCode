class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        nb_batteries = len(batteries)
        can_last = sum(batteries[:nb_batteries - n + 1])
        total_batteries = can_last
        for i in range(nb_batteries - n + 1, nb_batteries):
            total_batteries += batteries[i]
            if can_last >= batteries[i]:
                can_last = total_batteries // (i - nb_batteries + n + 1)
        return can_last

