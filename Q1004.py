class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l_ptr = 0
        best = 0
        count = 0
        for r_ptr in range(len(nums)):
            if nums[r_ptr] == 0:
                count += 1
            
            while count > k:
                if nums[l_ptr] == 0:
                    count -= 1
                l_ptr += 1

            best = max(best, r_ptr - l_ptr + 1)
        
        return best