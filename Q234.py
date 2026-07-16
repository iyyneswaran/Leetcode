# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            slow =  slow.next
            fast = fast.next.next
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True


# or  
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        return arr == arr[::-1]