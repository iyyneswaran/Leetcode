class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        curr_prefix = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            curr_prefix += num
            remainder = curr_prefix % k
            count += freq.get(remainder, 0)
            
            freq[remainder] = freq.get(remainder, 0) + 1
            
        return count