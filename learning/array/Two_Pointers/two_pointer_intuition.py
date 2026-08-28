def two_sum_sorted_array(arr, target):
    left, right = 0, len(arr)
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
