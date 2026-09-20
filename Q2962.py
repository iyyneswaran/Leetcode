class Solution:
    def subCheck(self, nums: List[int], k:int, maxE: int) -> int:
        l_ptr = 0
        count = 0
        res = 0
        for r_ptr, num in enumerate(nums):
            if num == maxE:
                count += 1
            while count > k:
                if nums[l_ptr] == maxE:
                    count -= 1
                l_ptr += 1
            res += r_ptr - l_ptr + 1

        return res

    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxE = max(nums)
        n = len(nums)
        return (n * (n + 1) // 2) - self.subCheck(nums, k - 1, maxE)