class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        t_sum = sum(nums)
        l_sum = 0
        for i, num in enumerate(nums):
            r_sum = t_sum - l_sum - num
            if l_sum == r_sum:
                return i
            l_sum += num
        
        return -1