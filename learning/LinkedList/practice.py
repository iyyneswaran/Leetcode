class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    # traversing
    def traversing(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')
    
    # insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    # insert at a specific location 
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        temp = self.head
        count = 0

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    # deletion at the beginning 
    def deletion_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next    
    
    # deletion at the end 
    def deletion_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # search in linked list 
    def search(self, key):
        temp = self.head
        index = 0
        while temp:
            if temp.data == key:
                return index
            index += 1
            temp = temp.next
        return "Element not found"

    # count nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


if __name__ == "__main__":
    ll = linkedList()
    ll.head = Node(20)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.insert_at_beginning(5)
    ll.insert_at_end(40)
    ll.insert_at_position(25, 2)
    ll.traversing()
