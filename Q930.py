class Solution:
    def atMostGoal(self, nums: list[int], goal: int) -> int:
        if goal < 0:
            return 0
            
        l_ptr = 0
        count = 0
        sumValue = 0
        for r_ptr, num in enumerate(nums):
            sumValue += num
            while sumValue > goal:
                sumValue -= nums[l_ptr]
                l_ptr += 1
            count += r_ptr - l_ptr + 1
        
        return count

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return self.atMostGoal(nums, goal) - self.atMostGoal(nums, goal - 1)