class Solution:
    def stoneGameVI(self, aliceValues: list[int], bobValues: list[int]) -> int:
        sorted_stones = sorted(zip(aliceValues, bobValues), key=lambda x: x[0] + x[1], reverse=True)
        a_score = 0
        b_score = 0
        for i in range(len(sorted_stones)):
            if i % 2 == 0:
                a_score += sorted_stones[i][0]
            else:
                b_score += sorted_stones[i][1]
        if a_score > b_score:
            return 1
        elif a_score < b_score:
            return -1
        else:
            return 0
