def floor_BS(nums: list[int], target: int) -> int:
    left = 0 
    right = len(nums) - 1

    if target > nums[right]:
        return nums[right]

    while  left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid

    return nums[left]



nums = list(map(int, input().split()))
target = int(input())
print(floor_BS(nums, target))