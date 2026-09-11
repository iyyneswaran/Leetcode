class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        bestSum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            bestSum = max(bestSum, window_sum)
        return bestSum / k