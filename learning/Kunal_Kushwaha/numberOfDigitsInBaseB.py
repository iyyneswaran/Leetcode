from math import log
n = int(input())
b = int(input())
ans = int(log(n)/ log(b)) + 1
print(ans)