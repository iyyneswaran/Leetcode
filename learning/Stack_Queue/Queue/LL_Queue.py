class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedlistQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return val

    def is_empty(self):
        return self.head is None

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.val
    