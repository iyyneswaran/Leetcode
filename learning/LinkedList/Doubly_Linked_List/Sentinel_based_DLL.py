class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _insert_between(self, data, prev_node, next_node):
        new = Node(data)
        new.prev = prev_node
        new.next = next_node
        prev_node.next = new
        next_node.prev = new

        return new

    def insert_beginning(self, data):
        self._insert_between(data, self.left, self.left.next)

    def insert_end(self, data):
        self._insert_between(data, self.right.prev, self.right)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

        return node.data

    def delete_value(self, value):
        curr = self.left.next
        while curr is not self.right:
            if curr.data == value:
                self._remove(curr)
                return True
            curr = curr.next

        return False

    def delete_by_index(self, index):
        if index < 0:
            raise IndexError("Invalid Index")

        curr = self.left.next
        position = 0
        while curr is not self.right:
            if position == index:
                self._remove(curr)
                return True
            curr = curr.next
            position += 1

        return False

    def display(self):
        curr = self.left.next
        while curr is not self.right:
            print(curr.data, end = "<->")
            curr = curr.next

        print("None")

dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_beginning(5)

dll.display()
# 5 <-> 10 <-> 20 <-> 30 <-> None

dll.delete_value(5)
dll.display()
# 10 <-> 20 <-> 30 <-> None

dll.delete_value(30)
dll.display()
# 10 <-> 20 <-> None