from heapq import heapify, heappop, heappush


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        length = len(target)
        if length == 1:
            return target[0] == 1
        current_sum = sum(target)
        target = [-k for k in target]
        heapify(target)
        while current_sum > length:
            element = -heappop(target)
            new_element = 1 + ((element - 1) % (current_sum - element))
            if new_element == element:
                return False
            heappush(target, -new_element)
            current_sum -= element - new_element
        return True

