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
    
    # insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert at end
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

    # deletion at beginning 
    def deletion_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next    
    
    # deletion at end 
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
    
    # find second middle of linked list 
    def find_second_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None
    
    # find first middle 
    def find_first_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return f"First middle is: {slow.data}" if slow else "No middle"

    # detect cycle in linked list 
    def cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "Cycle exists"
        return "No cycle exists"
    
    def reverse_linkedList(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    

if __name__ == "__main__":
    ll = linkedList()
    ll.head = Node(20)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.insert_at_beginning(5)
    ll.insert_at_end(40)
    ll.insert_at_position(25, 2)
    ll.traversing()
    print(ll.find_first_middle())
    print(ll.find_second_middle())