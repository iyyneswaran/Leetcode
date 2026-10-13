class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_prefix = 0
        freq = {0: 1}
        count = 0

        for num in nums:
            curr_prefix += num
            req = curr_prefix - k
            
            count += freq.get(req, 0)
            
            freq[curr_prefix] = freq.get(curr_prefix, 0) + 1
        
        return count