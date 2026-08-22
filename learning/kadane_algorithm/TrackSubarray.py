def max_subarray_with_indices(nums: List[int]):
    curr_sum = nums[0]
    max_sum = nums[0]
    start = 0
    best_start = best_end = 0
    for i in range(1, len(nums)):
        if nums[i] > curr_sum + nums[i]:
            curr_sum = nums[i]
            start = i
        else:
            curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start = start
            best_end = i
    return max_sum, nums[best_start: best_end + 1]