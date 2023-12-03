class Solution(object):
    def shiftingLetters(self, s, shifts):
        def one_shift(char_to_shift, nb_shifts):
            return chr(97 + (ord(char_to_shift) + nb_shifts - 97) % 26)
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in range(1, len(s)):
            shifts[-i-1] = (shifts[-i-1] + shifts[-i]) % 26
            shifts[-i] = one_shift(s[-i], shifts[-i])
        shifts[0] = one_shift(s[0], shifts[0])
        print(shifts)
        return "".join(shifts)
