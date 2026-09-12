# Longest subarray with sum less than equal to sumValue 

from typing import List

def longest_valid_window(nums: List[int], sumValue: int) -> int:
    left = 0
    best = 0
    window_sum = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > sumValue:
            window_sum -= nums[left]
            left += 1

        best = max(best, right - left + 1)

    return best

nums = list(map(int, input().split()))
sumValue = int(input())
print(longest_valid_window(nums, sumValue))