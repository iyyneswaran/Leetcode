class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # traversing forward
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        
    # traversing backward
    def display_backward(self):
        current = self.tail

        if current is None:
            return "Empty list"

        while current:
            print(current.data, end="<->")
            current = current.prev

    def insert_beginning(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
            return
        
        new.next = self.head
        self.head.prev = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.tail is None:
            self.head = self.tail = new
            return

        new.prev = self.tail
        self.tail.next = new
        self.tail = new

    # inserting a new node after a given node
    def insert_after(self, node, data):
        if self.node is None:
            return

        new_Node = Node(data)
        new_Node.prev = self.node
        new_Node.next = node.next

        if node.next:
            node.next.prev = new_Node

        node.next = new_Node

    def delete_value(self, value):
        current = self.head

        while current and current.data != value:
            current = current.next

        if current is None:
            return False
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        