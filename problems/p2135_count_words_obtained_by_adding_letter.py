class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        char_bitmask = {}
        current_digit = 1
        for i in range(97, 123):
            char_bitmask[chr(i)] = current_digit
            current_digit <<= 1
        startWords = set((sum((char_bitmask[char] for char in word)) for word in startWords))
        result = 0
        for target in targetWords:
            bitmask = 0
            for char in target:
                bitmask += char_bitmask[char]
            for char in target:
                bitmask -= char_bitmask[char]
                if bitmask in startWords:
                    result += 1
                    break
                bitmask += char_bitmask[char]
        return result
