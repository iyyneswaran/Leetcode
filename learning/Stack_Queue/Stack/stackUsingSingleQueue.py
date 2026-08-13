from collections import deque

class stackUsingSingleQueue:
    def __init__(self):
        self.q = deque()

    def push(self, val: int) -> None:
        self.q.append(val)
        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft())
    
    def pop(self) -> int:
        if not self.q:
            raise IndexError("Stack is empty")
        return self.q.popleft()

    def top(self) -> int:
        if not self.q:
            raise IndexError("Stack is empty")
        return self.q[0]

    def is_empty(self) -> bool:
        return not self.q

stack = stackUsingSingleQueue()
stack.push(1)
stack.push(2)
print(stack)
stack.pop()
stack.top()
stack.is_empty()
print(stack)