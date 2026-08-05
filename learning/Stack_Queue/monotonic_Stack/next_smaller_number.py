def increasingMS(nums: list) -> list:
    stack = []
    for digit in nums:
        while stack and stack[-1] > digit:
            stack.pop()
        stack.append(digit)
    return stack

nums = list(map(int, input().split()))
print(increasingMS(nums))