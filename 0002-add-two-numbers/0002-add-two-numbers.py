# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        last = None
        carry = False
        while l1 != None and l2 != None:
            sum_sl = l1.val + l2.val + 1 if carry else l1.val + l2.val
            carry = sum_sl > 9
            sum_sl = (sum_sl) % 10
            if ans == None:
                ans = ListNode(val=sum_sl, next=None)
                last = ans
            else:
                last.next = ListNode(val=sum_sl, next=None)
                last = last.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 != None else l2
        while l != None:
            sum_sl = l.val + 1 if carry else l.val
            carry = sum_sl > 9
            sum_sl = (sum_sl) % 10
            last.next = ListNode(val=sum_sl, next=None)
            last = last.next
            l = l.next
        if carry:
            last.next = ListNode(val=1, next=None)
        return ans