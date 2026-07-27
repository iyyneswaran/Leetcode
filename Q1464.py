class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_max = 0
        s_max = 0
        for num in nums:
            if num > s_max:
                f_max = s_max
                s_max = num
            elif num > f_max:
                f_max = num
        return (f_max - 1) * (s_max - 1)