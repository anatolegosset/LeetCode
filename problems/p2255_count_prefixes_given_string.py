class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        words.sort(key=len)
        print(words)
        i = 0
        for length in range(1, 11):
            current_str = s[:length]
            while i < len(words) and len(words[i]) == length:
                count += words[i] == current_str
                i += 1
        return count
