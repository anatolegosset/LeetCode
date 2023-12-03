from collections import deque


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        current_window = deque(s[:10])
        seen = {"".join(current_window): False}
        result = []
        for char in s[10:]:
            current_window.popleft()
            current_window.append(char)
            if (a := "".join(current_window)) in seen:
                if not seen[a]:
                    result.append(a)
                    seen[a] = True
            else:
                seen[a] = False
        return result
