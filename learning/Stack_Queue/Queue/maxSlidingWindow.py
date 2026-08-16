from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []

    for i, num in enumerate(nums):

        # 1. Remove indices that are outside the window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # 2. Remove smaller values from the back
        while dq and nums[dq[-1]] <= num:
            dq.pop()

        # 3. Add current index
        dq.append(i)

        # 4. Window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result