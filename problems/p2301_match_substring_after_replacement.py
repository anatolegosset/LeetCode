from collections import defaultdict


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        better_mapping = defaultdict(set)
        for char1, char2 in mappings:
            better_mapping[char1].add(char2)
        for i in range(len(s) - len(sub) + 1):
            flag = True
            for j, char in enumerate(sub):
                if s[i + j] not in better_mapping[char] and s[i + j] != char:
                    flag = False
                    break
            if flag:
                return True
        return False
