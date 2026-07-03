# Node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list creation
class LinkedList:
    def __init__(self):
        self.head = None

    # traversing 
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    

    # insert at beginning 
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

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.print_list()