from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_Deque = deque()
        max_Deque = deque()
        l_ptr = 0
        count = 0

        for r_ptr, num in enumerate(nums):
            while min_Deque and nums[min_Deque[-1]] > num:
                min_Deque.pop()
            min_Deque.append(r_ptr)

            while max_Deque and nums[max_Deque[-1]] < num:
                max_Deque.pop()
            max_Deque.append(r_ptr)

            while nums[max_Deque[0]] - nums[min_Deque[0]] > 2:
                if nums[min_Deque[0]] == nums[l_ptr]:
                    min_Deque.popleft()
                if nums[max_Deque[0]] == nums[l_ptr]:
                    max_Deque.popleft()

                l_ptr += 1
            
            count += r_ptr - l_ptr + 1
    
        return count