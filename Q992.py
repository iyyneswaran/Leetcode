class Solution:
    def distinctCount(self, nums: list[int], k: int) -> int:
        res = 0
        l_ptr = 0
        freq = {}
        for r_ptr, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            while len(freq) > k:
                freq[nums[l_ptr]] -= 1
                if freq[nums[l_ptr]] == 0:
                    del freq[nums[l_ptr]]
                l_ptr += 1

            res += r_ptr - l_ptr + 1

        return res

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.distinctCount(nums, k) - self.distinctCount(nums, k - 1)