from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        charset = Counter(chars)
        return sum(len(word) for word in words if Counter(word) <= charset)