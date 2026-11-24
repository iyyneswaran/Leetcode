class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_prod = 1
        right_prod = 1
        answer = [1] * n

        for i in range(len(nums)):
            answer[i] = left_prod
            left_prod *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_prod
            right_prod *= nums[i]
        
        return answer