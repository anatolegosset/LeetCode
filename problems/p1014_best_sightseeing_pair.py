class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        nb_values = len(values)
        maxes = [values[-1] - nb_values + 1]
        for i in range(1, nb_values - 1):
            val = values[-i-1]
            maxes.append(max(maxes[-1], val - nb_values + i + 1))

        max_pair = 0
        current_max = 0
        for i in range(nb_values - 1):
            new_max = max(current_max, values[i] + i)
            max_pair = max(max_pair, new_max + maxes[-i - 1])
        return max_pair


