from typing import List

def smallest_valid_window(nums: List[int], target: int) -> int:
    window_sum, left = 0, 0
    answer = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            answer = min(answer, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if answer == float('inf') else answer


nums = list(map(int, input().split()))
target = int(input())
print(smallest_valid_window(nums, target))