class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        result = []
        for start, end in zip(l, r):
            length = end - start
            s_max, s_min = nums[start], nums[start]
            for i in range(start + 1, end + 1):
                s_max = max(s_max, nums[i])
                s_min = min(s_min, nums[i])
            a, remain = (s_max - s_min) // length, (s_max - s_min) % length
            if remain > 0:
                result.append(False)
                continue
            if a == 0:
                result.append(True)
                continue
            seen = set()
            for i in range(start, end + 1):
                j, remain = (nums[i] - s_min) // a, (nums[i] - s_min) % a
                if remain > 0 or j in seen:
                    result.append(False)
                    break
                seen.add(j)
            if remain == 0 and len(seen) == length + 1:
                result.append(True)
        return result
