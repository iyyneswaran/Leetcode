class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_idx = 0
        self.rear_idx = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, val):
        if self.is_full():
            raise OverflowError("Queue is flow")
        self.rear_idx = (self.rear_idx + 1) % self.capacity
        self.arr[self.rear_idx] = val
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        val = self.arr[self.front_idx]
        self.arr[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.count -= 1
        return val

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.arr[self.front_idx]
