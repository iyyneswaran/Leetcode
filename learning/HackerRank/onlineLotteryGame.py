def removeDuplicates(arr):
    result = []
    seen = set()
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    result.sort(reverse=True)
    return result[0] + result[1]


n = int(input())
arr = list(map(int, input().split()))
print(removeDuplicates(arr))