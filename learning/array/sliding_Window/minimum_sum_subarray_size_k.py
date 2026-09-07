def minimumSum(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(arr):
        raise ValueError("Invalid window size")
    
    minimum_sum = float("inf")
    window_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        minimum_sum = min(minimum_sum, window_sum)

    return minimum_sum


nums = list(map(int, input().split()))
k = int(input())
(minimumSum(nums, k))