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

    