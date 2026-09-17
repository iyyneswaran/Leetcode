class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        l_ptr = 0
        product = 1
        result = 0
        for r_ptr in range(len(nums)):
            product *= nums[r_ptr]
            while product >= k:
                product //= nums[l_ptr]
                l_ptr += 1
            result += r_ptr - l_ptr + 1
        return result