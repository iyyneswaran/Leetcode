class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        answer, l_ptr = float('inf'), 0
        
        for r_ptr in range(len(nums)):
            window_sum += nums[r_ptr]
            while window_sum >= target:
                answer = min(answer, r_ptr - l_ptr + 1)
                window_sum -= nums[l_ptr]
                l_ptr += 1

        return 0 if answer == float('inf') else answer