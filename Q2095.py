# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _find_middle(self, head: ListNode | None) -> list:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None
        
        middle_node = self._find_middle(head)

        middle_node.next = middle_node.next.next
    
        return head
