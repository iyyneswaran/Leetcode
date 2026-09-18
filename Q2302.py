class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sumValue = 0
        l_ptr = 0
        count = 0
        for r_ptr, num in enumerate(nums):
            sumValue += num
            while sumValue * (r_ptr - l_ptr + 1) >= k:
                sumValue -= nums[l_ptr]
                l_ptr += 1

            count += r_ptr - l_ptr + 1

        return count