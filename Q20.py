class Solution:
    def isValid(self, s: str) -> bool:
        capacity = len(s)
        arr = [None] * capacity
        top = -1
        if capacity < 2:
            return False

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                top += 1
                arr[top] = ch
            else:
                if ch == ')' and arr[top] == '(':
                    arr[top] = None
                    top -= 1
                elif ch == ']' and arr[top] == '[':
                    arr[top] = None
                    top -= 1
                elif ch == '}' and arr[top] == '{':
                    arr[top] = None
                    top -= 1
                else:
                    return False
        return top == -1


# Approach 2:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack   