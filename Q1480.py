class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefixSum = []
        for i in range(len(nums)):
            if i == 0:
                prefixSum.append(nums[i])
            else:
                prefixSum.append(prefixSum[-1] + nums[i])

        return prefixSum