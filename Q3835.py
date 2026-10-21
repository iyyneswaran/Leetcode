from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_Deque = deque()
        min_Deque = deque()
        l_ptr = 0
        count = 0

        for r_ptr, num in enumerate(nums):
            while max_Deque and nums[max_Deque[-1]] < num:
                max_Deque.pop()
            max_Deque.append(r_ptr)

            while min_Deque and nums[min_Deque[-1]] > num:
                min_Deque.pop()
            min_Deque.append(r_ptr) 

            while (nums[max_Deque[0]] - nums[min_Deque[0]]) * (r_ptr - l_ptr + 1) > k:
                if nums[max_Deque[0]] == nums[l_ptr]:
                    max_Deque.popleft()
                if nums[min_Deque[0]] == nums[l_ptr]:
                    min_Deque.popleft()
                l_ptr += 1
                
            count += r_ptr - l_ptr + 1

        return count