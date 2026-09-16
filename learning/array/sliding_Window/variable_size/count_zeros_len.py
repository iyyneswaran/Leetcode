from typing import List

def zeros(nums: List[int]) -> int:
    count = 0
    left = 0
    best = float('inf')
    for right in range(len(nums)):
        if nums[right] == 1:
            count += 1
        while count >= 3:
            best = min(best, right - left + 1)
            out = nums[left]
            if out == 1:
                count -= 1
            left += 1 

    return 0 if best == float('inf') else best

nums = list(map(int, input().split()))
print(zeros(nums))