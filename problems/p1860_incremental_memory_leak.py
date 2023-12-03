class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        current_int = 1
        num1, num2 = memory1, memory2
        while num1 >= current_int or num2 >= current_int:
            if num1 >= num2:
                num1 -= current_int
            else:
                num2 -= current_int
            current_int += 1
        return [current_int, num1, num2]
