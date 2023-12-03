class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        neighbours = {i: [-1, []] for i in range(len(s))}
        for pair in pairs:
            neighbours[pair[0]][1].append(pair[1])
            neighbours[pair[1]][1].append(pair[0])
        current_cc = 0
        for i in range(len(s)):
            if neighbours[i][0] == -1 and neighbours[i][1]:
                neighbours[i][0] = current_cc
                to_visit = [i]
                while to_visit:
                    current_node = to_visit.pop()
                    for neighbour in neighbours[current_node][1]:
                        if neighbours[neighbour][0] == -1:
                            neighbours[neighbour][0] = current_cc
                            to_visit.append(neighbour)
                current_cc += 1
        substrings = {i: [] for i in range(current_cc)}
        for i, char in enumerate(s):
            if neighbours[i][0] > -1:
                substrings[neighbours[i][0]].append(char)

        for c in range(current_cc):
            substrings[c].sort(reverse=True)

        return ''.join((s[i] if neighbours[i][0] == -1 else substrings[neighbours[i][0]].pop() for i in range(len(s))))
