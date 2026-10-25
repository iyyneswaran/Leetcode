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

    # inserting a new node after a given node with value "data":
    def insert_after(self, node, data):
        if self.node is None:
            return

        new_Node = Node(data)
        new_Node.prev = self.node
        new_Node.next = node.next

        if node.next:
            node.next.prev = new_Node

        node.next = new_Node

    # inserting a new node in a specific index:
    def insert_at_index(self, data, index):
        if index < 0:
            return False
        
        if index == 0:
            self.insert_beginning(data)
            return True

        curr = self.head
        position = 0

        while curr and position < index:
            curr = curr.next
            position += 1

        if position != index:
            return False

        if curr is None:
            self.insert_end(data)
            return True

        new = Node(data)
        
        new.prev = curr.prev
        new.next = curr
        curr.prev.next = new
        curr.prev = new
            
        return True

    # delete a node with specific value:
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

        def delete_at_beginning(self):
            if self.head is None:
                return False

            removed = self.head
            self.head = removed.next

            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

            removed.next= None

            return True