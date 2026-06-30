def solution(arr):
    product = 0
    sumValue = 0
    for i in range(n-1):
        for j in range(n):
            if arr[i] * arr[j] > product:
                product = arr[i] * arr[j]
                sumValue = arr[i] + arr[j]
    return sumValue
     
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(solution(arr))