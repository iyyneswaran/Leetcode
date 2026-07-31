def nextPermutation(n, nums):
    # step 1: Find the pivot
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # step 2: If pivot exists,  find next larger element:
    if i >= 0:
        j = n- 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # step 3: Reverse the suffix
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right += 1

    return nums

length = int(input())
nums = list(map(int, input().split()))
print(nextPermutation(length, nums))