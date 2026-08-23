def max_subarray_circular(arr):
    total = sum(arr)

    # Case 1: normal Kadane's (max subarray, no wrap)
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    # Case 2: wrapping subarray = total - min subarray
    min_ending_here = min_so_far = arr[0]
    for x in arr[1:]:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    # Edge case: if ALL numbers are negative, total - min_so_far = 0 (empty),
    # which is invalid — in that case just return the normal max (max_so_far)
    if max_so_far < 0:
        return max_so_far

    return max(max_so_far, total - min_so_far)