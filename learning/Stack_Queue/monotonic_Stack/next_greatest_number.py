# method 1 
def decreasingMS(arr: list) -> list:
    stack = []
    for value in arr:
        while stack and stack[-1] < value:
            stack.pop()
        stack.append(value)

    return stack

# method 2
def decreasingMS2(arr: list) -> list:
    length = len(arr)
    result = [-1] * length
    stack = []

    for i in range(length):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result   


arr = list(map(int, input().split()))
print(decreasingMS(arr))
print(decreasingMS2(arr))
