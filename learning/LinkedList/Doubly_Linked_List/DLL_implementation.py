class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # traversing forward
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        
    # traversing backward
    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev

    def insert_beginning(self, data):
        new = Node(data)
        if self.head:
            new.next = self.head
            self.head.prev = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new
        new.prev = current