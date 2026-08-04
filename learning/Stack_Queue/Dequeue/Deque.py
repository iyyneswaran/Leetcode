class DNode:
    def __init__(self, val):
        self.val = val 
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, val):
        node = DNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def push_back(self, val):
        node = DNode(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail = node
        self._size += 1

    