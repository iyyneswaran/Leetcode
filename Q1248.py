class Solution:
    def oddCheck(self, nums: list[int], k: int) -> int:
        res = 0
        l_ptr = 0
        oddCount = 0
        for r_ptr, num in enumerate(nums):
            if (num & 1) == 1:
                oddCount += 1
            while oddCount > k:
                if (nums[l_ptr] & 1) == 1:
                    oddCount -= 1
                l_ptr += 1

            res += r_ptr - l_ptr + 1

        return res

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        return self.oddCheck(nums, k) - self.oddCheck(nums, k - 1)