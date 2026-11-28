class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        d = [False] * (n + 1)
        for i in nums:
            if d[i]:
                return i
            d[i] = True

# or 
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
        
        return -1

# or 
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return num
        
        return -1