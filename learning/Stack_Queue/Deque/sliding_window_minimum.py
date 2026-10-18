from collections import deque

def minimum_in_window(nums: list[int], k: int) -> list[int]:
    dq = deque()
    minValues = []

    for index, num in enumerate(nums):
        if dq and dq[0] <= index - k:
            dq.popleft()

        while dq and nums[dq[-1]] >= num:
            dq.pop()
        dq.append(index)

        if index >= k - 1:
            minValues.append(nums[dq[0]])

    return minValues


nums = list(map(int, input().split()))
k = int(input())
print(minimum_in_window(nums, k))
