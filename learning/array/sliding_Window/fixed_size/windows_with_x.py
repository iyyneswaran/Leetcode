def windows_with_target(nums, k, target):
    length = len(nums)

    if length < k or length <= 0:
        raise ValueError("Invalid Window Size K")

    count = 0
    
    window = nums[:k]
    for num in window:
        if num == target:
            count += 1
            break

    for i in range(k, length):
        if nums[i] == target:
            count += 1

    return count

nums = list(map(int, input().split()))
k = int(input())
target = int(input())
print(windows_with_target(nums, k, target))