class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums

        length = len(nums)
        window_length = k * 2 + 1
        ans = [-1] * length

        if length < window_length:
            return ans

        window_sum = sum(nums[:window_length])
        ans[k] = window_sum // window_length   

        for i in range(k + 1, length - k):
            window_sum = window_sum - nums[i - k - 1] + nums[i + k]        
            ans[i] = window_sum // window_length
        
        return ans
