class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_not_between = True
        count = 0
        for char in s:
            if char == '|':
                is_not_between = not is_not_between
            elif is_not_between and char == '*':
                count += 1
        return count
