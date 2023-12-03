from string import ascii_uppercase


class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        char_start, char_end = ascii_uppercase.index(s[0]), ascii_uppercase.index(s[3])
        num_start, num_end = int(s[1]), int(s[4])
        result = []

        for char in ascii_uppercase[char_start: char_end + 1 ]:
            for num in range(num_start, num_end + 1):
                result.append(char + str(num))

        return result
