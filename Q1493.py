class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        best_len = 0
        zeros_count = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros_count += 1

            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            best_len = max(best_len, right - left)
        
        return best_len