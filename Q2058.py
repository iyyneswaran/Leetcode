# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        slow = head
        temp = head.next
        fast = temp.next
        if fast is None:
            return [-1] * 2
        index = 2
        res = []
        while fast:
            if ((slow.val > temp.val) and (temp.val < fast.val)) or ((slow.val < temp.val) and (temp.val > fast.val)):
                res.append(index)
            index += 1
            slow = temp
            temp = fast
            fast = fast.next

        length = len(res)  

        if length < 2:
            return [-1] * 2

        maxDistance = res[-1] - res[0]
        
        minDistance = float('inf')
        for i in range(1, length):
            minDistance = min(minDistance, res[i] - res[i - 1])
        
        return [minDistance, maxDistance]