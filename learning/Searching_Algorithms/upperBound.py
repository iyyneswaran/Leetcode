def upper_bound(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

nums = [1, 2, 2, 2, 4, 6, 8]
last = upper_bound(nums, 2) - 1

print(last)