# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_set = set(nums)
        cur_pt = head
        prev_pt = None
        while(cur_pt):
            if cur_pt.val in nums_set:
                if prev_pt is None or cur_pt == head:
                    head = cur_pt.next
                else:
                    prev_pt.next = cur_pt.next
            else:
                prev_pt = cur_pt
            cur_pt = cur_pt.next
        return head