# Optimal approach using sliding window and monotonic deque => O(N)
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length



# Brute force - O(N^3) => pass 43/63 test cases [Worst one even God can't help]
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        length = len(nums)
        max_length = 0
        for i in range(length):
            left = i 
            while left < length:
                curr_window = nums[i:left+1]
                maxValue = max(curr_window)
                minValue = min(curr_window)
                diff = abs(maxValue - minValue)
                if diff <= limit:
                    max_length = max(len(curr_window), max_length)
                left += 1
        return max_length