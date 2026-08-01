class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1

    # add value in top
    def push(self, val):
        if self.top == self.capacity - 1:
            raise OverflowError("Stack Overflow")
        top += 1
        self.arr[self.top] = val

    # It removes the top value and return it
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        val = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return val