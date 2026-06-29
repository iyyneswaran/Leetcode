n = int(input())
arr = list(map(int, input().split()))

ans = arr[0]
for i in range(1, n):
    ans &= arr[i]

count = 0
while ans:
    ans &= (ans - 1)
    count += 1

print(count)