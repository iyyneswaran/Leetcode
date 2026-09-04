# Optimal
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
            
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
            
        prefix_max = float('-inf')
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            
            if prefix_max - suffix_min[i] <= k:
                return i
                
        return -1

# Brute force - bottle neck
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(0, n):
            if max(nums[:i + 1]) - min(nums[i:n]) <= k:
                return i
        return -1