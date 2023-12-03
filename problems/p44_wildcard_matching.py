from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def recursion(i, j):
            if j == len(p):
                return i == len(s)
            if i == len(s):
                return j == len(p) or set(p[j:]) == {'*'}
            if s[i] == p[j] or p[j] == '?':
                return recursion(i + 1, j + 1)
            if p[j] == '*':
                for k in range(i, len(s) + 1):
                    if recursion(k, j + 1):
                        return True
                return False
            return False
        return recursion(0, 0)
