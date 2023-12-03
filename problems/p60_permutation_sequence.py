class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        temp_code = k - 1
        current_step = n - 1
        while current_step > -1:
            temp_id, temp_code = temp_code // factorials[current_step], temp_code % factorials[current_step]
            for digit in range(1, 10):
                if digit not in result:
                    if temp_id == 0:
                        result.append(digit)
                        break
                    else:
                        temp_id -= 1
            current_step -= 1
        return "".join([str(digit) for digit in result])
