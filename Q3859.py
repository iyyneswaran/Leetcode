class Solution:
    def check(self, nums, k, m) -> int:
        res = 0
        freq = {}
        l_ptr = 0
        condition = False
        for r_ptr, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            while len(freq) > k:
                freq[nums[l_ptr]] -= 1
                if freq[nums[l_ptr]] >= m:
                    condition = True
                else:
                    condition = False

                if freq[nums[l_ptr]] == 0:
                    del freq[nums[l_ptr]]
                
                l_ptr += 1
            if len(freq) == k:
            # if condition:
                res += r_ptr - l_ptr + 1

        return res

    def countSubarrays(self, nums, k, m):
        return self.check(nums, k, m) - self.check(nums, k - 1, m)