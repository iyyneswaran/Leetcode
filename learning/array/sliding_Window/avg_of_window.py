def windowAverage(nums, k:int):
    length = len(nums)
    if  k <= 0 or length < k:
        raise ValueError("Invalid Index")
    result = [round(sum(nums[:k]) / k, 2)]

    for i in range(k, length):
        result.append(round(((k * result[-1]) - nums[i - k] + nums[i]) / k, 2))

    return result

nums = list(map(int, input().split()))
k = int(input())
print(windowAverage(nums, k))