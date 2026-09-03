# arr => array of elements
# k is the size of the window
# Sliding window: maintain a running sum, add the new element entering, subtract the one leaving.
def maxSum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    bestSum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        bestSum = max(bestSum, window_sum)
    return bestSum
