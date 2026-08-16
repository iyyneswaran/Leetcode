from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        maxValues = []

        for index, num in enumerate(nums):
            while dq and dq[0] <= index - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(index)

            if index >= k - 1:
                maxValues.append(nums[dq[0]])
        
        return maxValues