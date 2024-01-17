# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old_node = None
        while(head):
            new_node = ListNode(head.val)
            new_node.next = old_node
            old_node = new_node
            head = head.next
        if old_node == None:
            return None
        return new_node
            
            