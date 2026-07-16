# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 != p2:

            if p1:
                p1 = p1.next
            else:
                p1 = headB

            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1

# or

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        isVisited = set()
        tempA = headA
        while tempA:
            isVisited.add(tempA)
            tempA = tempA.next
        
        tempB = headB
        while tempB:
            if tempB in isVisited:
                return tempB
            tempB = tempB.next

        return None
        