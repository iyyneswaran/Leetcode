arr = [1, 5, 3, 6, 8]
length = len(arr)
prefix = [0] * length # creates [0, 0, 0, 0, 0]
prefix[0] = arr[0]
for i in range(1, length):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)

l = 2
r = 3

if l == 0:
    ans = prefix[r]
else:
    ans = prefix[r] - prefix[l-1]
print(ans)