class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def traversing(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    def remove_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove(self, position):

        if self.head is None:
            return 'list is empty'
        
        if position < 0:
            return 'Invalid position'
        
        if position == 0:
            self.remove_at_beginning()
            return 'Successfully removed 1st node'
        
        prev = self.head
        curr = prev.next
        count = 1

        while curr is not None:
            if count == position:
                prev.next = curr.next
                return f'{position} is removed Successfully'
            prev = curr
            curr = curr.next
            count += 1

        return "Position out of range"

if __name__ == '__main__':
    ll = Linkedlist()
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.head.next.next.next = Node(40)
    ll.head.next.next.next.next = Node(50)
    print(ll.remove(3))
    ll.traversing()
