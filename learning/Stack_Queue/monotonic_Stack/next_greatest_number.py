def decreasingMS(arr):
    stack = []
    for value in arr:
        while stack and stack[-1] < value:
            stack.pop()
        stack.append(value)

    return stack

arr = list(map(int, input().split()))
print(decreasingMS(arr))