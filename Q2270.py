class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        t_sum = sum(nums)
        count = 0
        l_sum = 0
        for num in range(len(nums) - 1):
            l_sum += nums[num]
            if l_sum >= (t_sum - l_sum):
                count += 1
        return count