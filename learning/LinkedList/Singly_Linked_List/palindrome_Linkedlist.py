class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
    
    # insert new value in the end
    def append(self, val):
        new_Node = ListNode(val)
        
        if self.head is None:
            self.head = new_Node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_Node
    
    # to display the linked list made 
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=' -> ')
            temp = temp.next
        print('None')

    # check whether a linked list is palindrome or not
    def isPalindrome(self):
        if self.head is None or self.head.next is None:
            return True
        
        # find the middle
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # compare first and second half:
        first = self.head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

if __name__ == '__main__':
    ll = linkedList()
    n = int(input())
    for _ in range(n):
        ll.append(int(input()))
    ll.display()
    print('Palindrome' if ll.isPalindrome() else 'Not a palindrome')
