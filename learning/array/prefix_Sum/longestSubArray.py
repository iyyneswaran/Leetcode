
def maxSubArrayLen(nums, k):
    current_prefix = 0
    max_length = 0

    first_seen = {0: -1}

    for i, num in enumerate(nums):
        current_prefix += num

        required = current_prefix - k

        if required in first_seen:
            length = i - first_seen[required]
            max_length = max(max_length, length)

        if current_prefix not in first_seen:
            first_seen[current_prefix] = i

    return max_length


nums = [1, -1, 5, -2, 3]
k = 3

print(maxSubArrayLen(nums, k))  # 4
