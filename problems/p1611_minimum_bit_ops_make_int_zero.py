class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def recursion(a, target):
            if a == target:
                return 0
            elif a == 0:
                return 2 * target - 1
            elif target == 0 and a.bit_count() == 1:
                return 2 * a - 1
            elif target and a >= target:
                return recursion(a - target, 0)
            else:
                power = 2 ** (max(a, target).bit_length() - 1)
                return power + recursion(a % power, target=power // 2)

        return recursion(n, 0)
