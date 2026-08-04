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

    def pop_front(self):
        if not self.head:
            raise IndexError("Deque is empty")
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val
    
    def pop_back(self):
        if not self.tail:
            raise IndexError("Deque is empty")
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    
 