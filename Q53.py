# Optimal solution: O(n):
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            currSum += num
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(maxSum, currSum)

        return maxSum


# Brute force: O(n^2):
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum += nums[j]
                maxSum = max(currSum, maxSum)
        return maxSum