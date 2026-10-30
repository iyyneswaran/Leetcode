def lower_bound(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)  # Exclusive boundary
    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

nums = [1, 2, 2, 2, 4, 6, 8]
target = 2
first = lower_bound(nums, 2)

if first == len(nums) or nums[first] != target:
    print([-1, -1])
else:
    print(first)