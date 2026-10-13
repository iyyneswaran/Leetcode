class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        curr_prefix = 0
        seen = {0: -1}

        for i, num in enumerate(nums):
            curr_prefix += num
            remainder = curr_prefix % k
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
                
        return False