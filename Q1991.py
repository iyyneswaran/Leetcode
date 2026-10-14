class Solution:
    def buildPrefixSum(self, nums: list[int]):
        prefixSum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefixSum[i + 1] = prefixSum[i] + num

        return prefixSum 


    def findMiddleIndex(self, nums: list[int]) -> int:
        prefixSum = self.buildPrefixSum(nums)

        for i in range(1, len(prefixSum)):
            left_sum = prefixSum[i - 1]
            right_sum = prefixSum[-1] - prefixSum[i]
            
            if left_sum == right_sum:
                return i - 1
        
        return -1