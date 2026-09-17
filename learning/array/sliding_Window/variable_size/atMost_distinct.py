from typing import List

def atMost_distinct(arr: List[int], k: int) -> int:
    freq = {}
    count = 0
    left = 0
    distinct = len(freq)
    for right in range(len(arr)):
        if arr[right] in freq:
            freq[arr[right]] += 1
        else:
            freq[arr[right]] = 1
            distinct += 1
        while distinct > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
                distinct -= 1
            left += 1
        count += right - left + 1 
    return count


arr = list(map(int, input().split()))
k = int(input())
print(atMost_distinct(arr, k))