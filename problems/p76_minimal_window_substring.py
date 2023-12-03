from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        current = Counter()
        start, end = 0, 0
        best_start, best_end = 0, len(s) + 1
        while end < len(s) or target <= current:
            if target <= current:
                if end - start < best_end - best_start:
                    best_start, best_end = start, end
                if (c := s[start]) in target:
                    current[c] -= 1
                start += 1
            else:
                if (c := s[end]) in target:
                    current[c] += 1
                end += 1

        if best_end == len(s) + 1:
            return ""
        else:
            return s[best_start:best_end]


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
