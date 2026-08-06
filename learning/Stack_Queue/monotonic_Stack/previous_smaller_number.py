def previous_smaller_number(nums: list) -> list:
    stack = []
    ans = []
    for x in nums:
        while stack and stack[-1] >= x:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(x)
    return ans

nums = list(map(int, input().split()))
print(previous_smaller_number(nums))