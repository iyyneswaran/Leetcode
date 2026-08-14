# using array
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * self.capacity
        self.front_idx = 0
        self.rear_idx = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear_idx = (self.rear_idx + 1) % self.capacity
        self.queue[self.rear_idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        value = self.queue[self.front_idx]
        self.queue[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear_idx]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



# Using singly linked list 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = k
        self.freeSpace = 0

    def enQueue(self, value: int) -> bool:
        new_node = Node(value)
        if self.isFull():
            return False
        if self.tail is None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.freeSpace += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.freeSpace -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.head is None

    def isFull(self) -> bool:
        return self.freeSpace == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



# Top 100% by eliminating action of garbage collector:
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        
        self.head = Node()
        curr = self.head
        for _ in range(k - 1):
            curr.next = Node()
            curr = curr.next
        curr.next = self.head
        
        self.tail = self.head 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.count == 0:
            self.head.value = value
            self.tail = self.head
        else:
            self.tail = self.tail.next
            self.tail.value = value
            
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity