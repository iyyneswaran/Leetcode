class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedListStack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, val):
        node = Node(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        self._size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("Stack underflow")

        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self._size -= 1
        return val

    def peek(self):
        if self.head is None:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size