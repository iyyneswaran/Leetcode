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