class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [''] * len(s)
        top = -1
        for ch in s:
            if top == -1 or stack[top] != ch:
                top += 1
                stack[top] = ch
            else:
                stack[top] = ''
                top -= 1
        return ''.join(stack[:top + 1])

# optimal approach
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for ch in s:
            if stack and stack[-1]==ch:
               stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)      
