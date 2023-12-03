from collections import deque


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            quotient = num // (valueDiff + 1)
            if quotient in last_seen:
                while last_seen[quotient] and i - last_seen[quotient][0] > indexDiff:
                    last_seen[quotient].popleft()
                for previous in last_seen[quotient]:
                    if abs(nums[previous] - num) <= valueDiff:
                        return True
            else:
                last_seen[quotient] = deque()
            last_seen[quotient].append(i)
            quotient += 1
            if quotient in last_seen:
                while last_seen[quotient] and i - last_seen[quotient][0] > indexDiff:
                    last_seen[quotient].popleft()
                for previous in last_seen[quotient]:
                    if abs(nums[previous] - num) <= valueDiff:
                        return True
            else:
                last_seen[quotient] = deque()
            last_seen[quotient].append(i)
        return False
