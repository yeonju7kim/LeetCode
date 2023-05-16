# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        left = head
        right = head.next
        if right:
            head = right
        while left != None and right != None:
            left.next = right.next
            right.next = left
            next_left = left.next
            if left.next != None:
                if left.next.next!= None:
                    left.next = left.next.next
            else:
                left.next = None
            left = next_left
            if left:
                right = left.next
        return head