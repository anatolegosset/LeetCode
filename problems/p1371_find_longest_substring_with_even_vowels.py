class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        left_side = {0: -1}
        current_bitmask = 0
        current_max = 0
        for i, char in enumerate(s):
            if char in vowels:
                current_bitmask ^= vowels[char]
                left_side.setdefault(current_bitmask, i)
            current_max = max(current_max, i - left_side[current_bitmask])
        return current_max
