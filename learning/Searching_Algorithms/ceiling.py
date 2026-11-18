def ceiling_element_BS(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return nums[left]

nums = list(map(int, input().split()))
target = int(input())
print(ceiling_element_BS(nums, target))
