from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        sample = deque()
        for i in range(0, len(deck)):
            sample.appendleft(deck.pop())
            if deck:
                sample.appendleft(sample.pop())
        return list(sample)
