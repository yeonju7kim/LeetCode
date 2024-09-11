# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_common_divisor(a, b):
    smaller = a if a < b else b
    common_divisor = 1
    for i in range(2, smaller + 1):
        if a % i == 0 and b % i == 0:
            common_divisor = i
    return common_divisor

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = head
        cur = head.next
        while(cur):
            v = get_common_divisor(prev.val, cur.val)
            prev.next = ListNode(val = v, next = cur)
            prev = cur
            cur = cur.next
            
        return head

