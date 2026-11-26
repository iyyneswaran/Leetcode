# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _middle(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _reverse(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


    def pairSum(self, head: ListNode | None) -> int:
        middle_node = self._middle(head)

        second_half = self._reverse(middle_node)

        first_half = head
        max_sum = 0

        while second_half:
            curr_sum = first_half.val + second_half.val
            max_sum = max(curr_sum, max_sum)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum