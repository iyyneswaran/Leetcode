class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        init_avg = sum(arr[:k]) / k
        count = 0
        if init_avg >= threshold:
            count = 1
        for i in range(k, len(arr)):
            init_avg = ((k * init_avg) + arr[i] - arr[i - k]) / k
            if init_avg >= threshold:
                count += 1
        return count