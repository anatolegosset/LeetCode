from collections import Counter


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        letters = Counter(letters)
        words = [(Counter(word), sum((score[ord(char) - 97] for char in word))) for word in words if Counter(word) <= letters]
        max_score = max([word[1] for word in words] or [0])
        nb_words = len(words)
        previous_sets = list(enumerate(words))
        for _ in range(nb_words):
            new_sets = []
            for i, (c_set, s_set) in previous_sets:
                for j in range(i + 1, nb_words):
                    if (c_set + words[j][0]) <= letters:
                        new_sets.append((j, (c_set + words[j][0], s_set + words[j][1])))
                        max_score = max(max_score, new_sets[-1][1][1])
            if not new_sets:
                break
            previous_sets = new_sets
        return max_score




        