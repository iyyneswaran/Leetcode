class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct_idx = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

# or 
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        
        for x in range(1, n + 2):
            if x not in num_set:
                return x
            



