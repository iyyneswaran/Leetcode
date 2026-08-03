class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # add value to the linked list stack
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.val
    